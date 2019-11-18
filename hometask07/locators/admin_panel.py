# Python 3.6
# encoding: utf-8

""" Locators of administrator panel. """
from hometask07.locators.common_selectors import CSS


class AdminPanel:
    """ CSS selectors used. """

    class NavigationMenu:
        """ Items of navigation menu. """

        catalog = (CSS, '#menu-catalog')

        class Catalog:
            """ Items of Catalog submenu. """

            products = (CSS, '#collapse1 > li:nth-child(2) > a:nth-child(1)')

    add_button = (CSS, 'a.btn:nth-child(2)')
    copy_button = (CSS, 'button.btn:nth-child(3)')
    remove_button = (CSS, 'button.btn:nth-child(4)')

    class ProductList:
        """ Product list table. """

        check_all = (CSS, '.table > thead:nth-child(1) > tr:nth-child(1) > td:nth-child(1)')
        table_body = (CSS, '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)')
        product_name = (CSS, '.table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)')
        search_results_count = (CSS, 'div.col-sm-6:nth-child(2)')
        edit_button = (CSS, 'a.btn:nth-child(1)')

    class AddProductPage:
        """ Elements of adding product page. """

        product_name_input = (CSS, '#input-name1')
        meta_tag_title_input = (CSS, '#input-meta-title1')
        save_button = (CSS, 'div.pull-right > button:nth-child(1)')
        data_tab = (CSS, '#form-product > ul:nth-child(1) > li:nth-child(2)')
        model_input = (CSS, '#input-model')
        notification_message = (CSS, '.alert')

    class Filter:
        """ Filtering of the products list. """

        product_name_input = (CSS, '#input-name')
        filter_button = (CSS, '#button-filter')
