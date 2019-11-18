# Python 3.6
# encoding: utf-8

""" Configuration file. """

import os

import pytest
from selenium import webdriver

from hometask07.locators.admin_login_page import AdminLoginPage
from hometask07.locators.admin_panel import AdminPanel


def pytest_addoption(parser):
    """ You can specify URL and browser by this options. """

    parser.addoption('--browser', '-B',
                     action='store',
                     default='firefox',
                     help="choose your browser")
    parser.addoption('--url', '-U',
                     action='store',
                     default='http://localhost/opencart/admin/',
                     help="choose your URL")


@pytest.fixture
def browser(request):
    """ Webdriver's settings. """

    browser_param = request.config.getoption('--browser')
    if browser_param == 'chrome':
        driver = webdriver.Chrome(os.path.join(os.path.curdir, 'webdrivers', 'chromedriver'))
    elif browser_param == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{request.param} is not supported!")

    request.addfinalizer(driver.close)

    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get(request.config.getoption('--url'))

    return driver


def log_in(bro, user='admin', password='admin'):
    """ Logging in. """

    bro.find_element(*AdminLoginPage.username_field).send_keys(user)
    bro.find_element(*AdminLoginPage.password_field).send_keys(password)
    bro.find_element(*AdminLoginPage.login_button).click()


def create_product(bro, product_name):
    """ Creating of the product. """

    bro.find_element(*AdminPanel.NavigationMenu.catalog).click()
    bro.find_element(*AdminPanel.NavigationMenu.Catalog.products).click()
    bro.find_element(*AdminPanel.add_button).click()
    bro.find_element(*AdminPanel.AddProductPage.product_name_input).send_keys(product_name)
    bro.find_element(*AdminPanel.AddProductPage.meta_tag_title_input).send_keys(product_name)
    bro.find_element(*AdminPanel.AddProductPage.data_tab).click()
    bro.find_element(*AdminPanel.AddProductPage.model_input).send_keys(product_name)
    bro.find_element(*AdminPanel.AddProductPage.save_button).click()


def delete_product(bro, product_name):
    """ Deleting of the product. """

    if not bro.find_element(*AdminPanel.NavigationMenu.Catalog.products).is_displayed():
        bro.find_element(*AdminPanel.NavigationMenu.catalog).click()
    bro.find_element(*AdminPanel.NavigationMenu.Catalog.products).click()
    product_filter(bro, product_name)
    bro.find_element(*AdminPanel.ProductList.check_all).click()
    bro.find_element(*AdminPanel.remove_button).click()
    bro.switch_to.alert.accept()


def product_filter(bro, product_name):
    """ Filtering product list by product name. """

    bro.find_element(*AdminPanel.Filter.product_name_input).send_keys(product_name)
    bro.find_element(*AdminPanel.Filter.filter_button).click()
