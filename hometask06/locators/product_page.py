# Python 3.6
# encoding: utf-8

""" Locators of product page. """


class ProductPage:

    """ CSS selectors used. """

    breadcrumbs = 'ul.breadcrumb > li'
    thumbnails = '.thumbnails > li'
    item_summary = 'div.col-sm-4:nth-child(2)'
    tabs = 'ul.nav > li'
    review = '#review'
