# -*- coding: UTF-8 -*-

"""Tests divided into two parts for demonstrating 'module' scope."""


def test_exponentiation(session_fixture, module_fixture, function_fixture):

    """This test checks exponentiation of integers."""

    a = b = 2
    assert a ** b == 4, "Exponentiation doesn't work."


def test_lists(session_fixture, module_fixture, function_fixture):

    """This test checks search in a list."""

    letters = ('x', 'y', 'z')
    assert 'x' in letters, "Search in list doesn't work."


def test_dictionaries(session_fixture, module_fixture, function_fixture):

    """This test checks association in a key-value pair."""

    alphabet = {'A': 'alpha', 'B': 'beta', 'G': 'logic'}
    assert alphabet['G'] == 'logic', "G - logic!"


def test_tuples(session_fixture, module_fixture, function_fixture):

    """This test checks indices in tuple."""

    t = 12345, 54321, 'Hello!'
    assert t[1] == 54321, "Indices don't work."


def test_sets(session_fixture, module_fixture, function_fixture):

    """This test checks set method."""

    numbers = 1, 2, 8, 9, 2, 9
    assert len(set(numbers)) == 4, "Set method doesn't work."
