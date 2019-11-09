# Python 3.6
# encoding: utf-8

""" Locators of of header of pages. """


class Footer:

    """ CSS selectors used. """

    information = 'ul.list-unstyled > li'
    powered_by = 'body > footer:nth-child(5) > div:nth-child(1) > p:nth-child(3) > a:nth-child(1)'
