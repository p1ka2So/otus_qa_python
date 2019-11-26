# Python 3.6
# encoding: utf-8

""" Configuration file. """

import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """ You can specify URL and browser by this options. """

    parser.addoption('--browser', '-B',
                     action='store',
                     default='firefox',
                     help="choose your browser")
    parser.addoption('--url', '-U',
                     action='store',
                     default='https://code.makery.ch/library/dart-drag-and-drop/',
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
