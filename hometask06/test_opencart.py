# Python 3.6
# encoding: utf-8

""" Hometask 06. Searching web elements. """

import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from hometask06.locators.admin_login_page import AdminLoginPage
from hometask06.locators.header import Header
from hometask06.locators.main_page import MainPage
from hometask06.locators.product_page import ProductPage


def test_currency(browser):

    """ Check changing currency symbol. """

    browser.find_element(By.CSS_SELECTOR, Header.Menu.currency).click()
    currencies = browser.find_elements(By.CSS_SELECTOR, Header.Menu.currencies)
    for currency in currencies:
        if currency.text == '£ Pound Sterling':
            currency.click()
            break
    assert browser.find_element(By.CSS_SELECTOR, Header.Menu.currency_symbol).text == '£'


def test_breadscrumbs(browser):

    """ Check breadscrumbs in catalog section. """

    section = 'Components'
    component = 'Monitors'
    components_link = browser.find_element(By.CSS_SELECTOR, Header.NavigationBar.components_link)
    ActionChains(browser).move_to_element(components_link).pause(1).perform()
    components_list = browser.find_elements(By.CSS_SELECTOR, Header.NavigationBar.components_list)
    for item in components_list:
        if re.match(fr'^{component} \(\d+\)$', item.text):
            ActionChains(browser).move_to_element(item).click().perform()
            break
    breadscrumbs = browser.find_elements(By.CSS_SELECTOR, ProductPage.breadcrumbs)
    assert breadscrumbs[1].text == section, f"Breadscrumb {section} not found."
    assert breadscrumbs[2].text == component, f"Breadscrumb {component} not found."


def test_add_to_cart(browser):

    """ Check label of cart button. """

    featured = browser.find_elements(By.CSS_SELECTOR, MainPage.featured)
    for item in featured:
        item_name = item.find_element(By.CSS_SELECTOR, MainPage.ProductLayout.item_name)
        if item_name.text == 'iPhone':
            item.find_element(By.CSS_SELECTOR, MainPage.ProductLayout.add_item_btn).click()
            break
    time.sleep(1)
    cart_total = browser.find_element(By.CSS_SELECTOR, Header.cart)
    assert re.match(r'^1 item\(s\) - \$\d+\.\d+$', cart_total.text), "Item not added to cart."


def test_no_product_review(browser):

    """ Check no reviews. """

    featured = browser.find_elements(By.CSS_SELECTOR, MainPage.featured)
    for item in featured:
        item_name = item.find_element(By.CSS_SELECTOR, MainPage.ProductLayout.item_name)
        if item_name.text == 'Canon EOS 5D':
            item.find_element(By.CSS_SELECTOR, MainPage.ProductLayout.item_picture).click()
            break
    tabs = browser.find_elements(By.CSS_SELECTOR, ProductPage.tabs)
    for tab in tabs:
        if tab.text == 'Reviews (0)':
            tab.click()
            break
    text = browser.find_element(By.CSS_SELECTOR, ProductPage.review).text
    assert text == 'There are no reviews for this product.', "There must be no reviews."


def test_admin_login(browser):

    """ Check title of admin page. """

    browser.get('http://localhost/opencart/admin/')
    browser.find_element(By.CSS_SELECTOR, AdminLoginPage.username_field).send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, AdminLoginPage.password_field).send_keys('admin')
    browser.find_element(By.CSS_SELECTOR, AdminLoginPage.login_button).click()
    assert browser.title == 'Dashboard', "Title must be \"Dushboard\""
