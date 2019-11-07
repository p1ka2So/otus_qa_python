# Python 3.6
# encoding: utf-8
import re
import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from hometask06.locators.Header import Header
from hometask06.locators.MainPage import MainPage
from hometask06.locators.ProductPage import ProductPage


def test_currency(browser):
    browser.find_element(By.CSS_SELECTOR, Header.Menu.currency).click()
    currencies = browser.find_elements(By.CSS_SELECTOR, Header.Menu.currencies)
    for currency in currencies:
        if currency.text == '£ Pound Sterling':
            currency.click()
            break
    assert browser.find_element(By.CSS_SELECTOR, Header.Menu.currency_symbol).text == '£', "Currency not in Pounds."


def test_breadscrumbs(browser):
    component = 'Monitors'
    components_link = browser.find_element(By.CSS_SELECTOR, Header.NavigationBar.components_link)
    ActionChains(browser).move_to_element(components_link).pause(1).perform()
    components_list = browser.find_elements(By.CSS_SELECTOR, Header.NavigationBar.components_list)
    for item in components_list:
        if re.match(fr'^{component} \(\d+\)$', item.text):
            ActionChains(browser).move_to_element(item).click().perform()
            break
    breadscrumbs = browser.find_elements(By.CSS_SELECTOR, ProductPage.breadcrumbs)
    assert breadscrumbs[1].text == 'Components', "Breadscrumb \"Components\" not found."
    assert breadscrumbs[2].text == component, f"Breadscrumb {component} not found."


def test_add_to_cart(browser):
    featured = browser.find_elements(By.CSS_SELECTOR, MainPage.featured)
    for item in featured:
        item_name = item.find_element(By.CSS_SELECTOR, MainPage.ProductLayout.item_name)
        if item_name.text == 'iPhone':
            item.find_element(By.CSS_SELECTOR, MainPage.ProductLayout.add_item_btn).click()
            break
    time.sleep(5)
    cart_total = browser.find_element(By.CSS_SELECTOR, Header.cart)
    assert re.match(r'^1 item\(s\) - \$\d+\.\d+$', cart_total.text), "Item not added to cart."
