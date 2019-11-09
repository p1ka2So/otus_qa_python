# Python 3.6
# encoding: utf-8

""" Locators of main page. """


class MainPage:

    """ CSS selectors used. """

    big_promoblock = 'slideshow0'
    small_promoblock = 'carousel0'
    featured = 'div.row:nth-child(4) > div'

    class ProductLayout:

        """ An item in a Featured block """

        item_name = 'h4:nth-child(1)'
        add_item_btn = 'button:nth-child(1)'
        item_picture = 'img:nth-child(1)'
