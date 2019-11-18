# Python 3.6
# encoding: utf-8

""" Hometask 06. Searching web elements. """

import pytest

from hometask07.conftest import log_in, delete_product, product_filter, create_product
from hometask07.locators.admin_panel import AdminPanel


@pytest.mark.parametrize('product_name', ['Honor P20'])
def test_adding_product(browser, product_name):
    """ Adding a product. """

    log_in(browser)
    create_product(browser, product_name)

    product_filter(browser, product_name)
    search_results = browser.find_element(*AdminPanel.ProductList.product_name).text
    assert search_results == product_name, f"Should be a result for searching {product_name}."
    search_results_count = browser.find_element(*AdminPanel.ProductList.search_results_count).text
    assert search_results_count == 'Showing 1 to 1 of 1 (1 Pages)', "Should be found 1 product."

    delete_product(browser, product_name)


@pytest.mark.parametrize('product_name', ['Honor P20'])
def test_deleting_product(browser, product_name):
    """ Deleting a product. """

    log_in(browser)
    create_product(browser, product_name)

    delete_product(browser, product_name)
    product_filter(browser, product_name)
    search_results = browser.find_element(*AdminPanel.ProductList.table_body).text
    assert search_results == 'No results!', f"Should be no results for searching {product_name}."


@pytest.mark.parametrize('product_name', ['Honor P20'])
def test_editing_product(browser, product_name):
    """ Editing a product. """

    log_in(browser)
    create_product(browser, product_name)

    product_filter(browser, product_name)
    browser.find_element(*AdminPanel.ProductList.edit_button).click()
    browser.find_element(*AdminPanel.AddProductPage.product_name_input).send_keys(' EDITED')
    browser.find_element(*AdminPanel.AddProductPage.save_button).click()
    search_results = browser.find_element(*AdminPanel.ProductList.product_name).text
    assert search_results == product_name + ' EDITED', \
        f"\"{product_name} EDITED\" should be found."

    delete_product(browser, product_name + ' EDITED')
