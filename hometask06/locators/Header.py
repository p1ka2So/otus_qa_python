# Python 3.6
# encoding: utf-8


class Header:

    class Menu:
        currency = '#form-currency > div:nth-child(1) > button:nth-child(1) > span:nth-child(2)'
        currency_symbol = '#form-currency > div:nth-child(1) > button:nth-child(1) > strong:nth-child(1)'
        currencies = '.open > ul:nth-child(2) > li'
        top_links = 'ul.list-inline > li'

    class NavigationBar:
        nav_links = 'ul.nav > li'
        components_link = 'li.dropdown:nth-child(3) > a:nth-child(1)'
        components_list = 'li.dropdown:nth-child(3) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li'

    class Search:
        search_field = 'input.form-control:nth-child(1)'
        search_button = '.input-group-btn'

    logo = '#logo > h1:nth-child(1) > a:nth-child(1)'
    cart = '#cart-total'
