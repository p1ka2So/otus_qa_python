# Python 3.6
# encoding: utf-8

""" Hometask 08. Actions with web elements. """

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_drag_n_drop(browser):
    """ Testing drag'n'drop action. """

    browser.execute_script('window.scrollTo(0, 600)')
    frame = browser.find_element(By.CSS_SELECTOR, '.article-content > iframe:nth-child(9)')
    browser.switch_to.frame(frame)
    target = browser.find_element(By.CSS_SELECTOR, '.trash')
    elements = browser.find_elements(By.CSS_SELECTOR, '.document')
    for element in elements:
        ActionChains(browser).drag_and_drop(element, target).perform()
