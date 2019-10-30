# Python 3.6
# encoding: utf-8


def test_opencart(browser):
    """ Checking that we at OpenCart page. """
    url = 'http://localhost/opencart/index.php?route=common/home'
    assert browser.find_element_by_xpath(f'//a[@href="{url}"]').text == 'Your Store'
