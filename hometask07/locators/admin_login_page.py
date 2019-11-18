# Python 3.6
# encoding: utf-8

""" Locators of administrator login page. """
from hometask07.locators.common_selectors import CSS


class AdminLoginPage:
    """ CSS selectors used. """

    username_field = (CSS, '#input-username')
    password_field = (CSS, '#input-password')
    forgotten_password = (CSS, '.help-block > a:nth-child(1)')
    login_button = (CSS, '.btn')
