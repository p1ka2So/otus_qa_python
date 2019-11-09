# Python 3.6
# encoding: utf-8

""" Locators of catalog page. """


class CatalogPage:

    """ CSS selectors used. """

    breadcrumb = 'ul.breadcrumb > li'
    list_group = '.list-group'
    banner = '.swiper-viewport'
    refine_search = 'div.row:nth-child(3)'
    display_settings = 'div.row:nth-child(4)'
    items = 'div.row:nth-child(5)'
    pagination = 'div.row:nth-child(6)'
