# Python 3.6
# encoding: utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from hometask06.locators.Header import Header
from hometask06.locators.MainPage import MainPage


def test_currency(browser):
    browser.find_element(By.CSS_SELECTOR, Header.Menu.currency).click()
    currencies = browser.find_elements(By.CSS_SELECTOR, Header.Menu.currencies)
    for currency in currencies:
        if currency.text == '£ Pound Sterling':
            currency.click()
            break
    assert browser.find_element(By.CSS_SELECTOR, Header.Menu.currency_symbol).text == '£', "Need more pounds."


def test_breadscrumbs(browser):
    menu_links = browser.find_elements(By.CSS_SELECTOR, Header.NavigationBar.nav_links)
    components_link = ''
    for link in menu_links:
        if link.text == 'Components':
            components_link = link
            break
    ActionChains(browser).move_to_element(components_link).pause(2).perform()
