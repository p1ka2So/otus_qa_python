# -*- coding: UTF-8 -*-

"""Tests divided into two parts for demonstrating 'module' scope."""


def test_strings(session_fixture, module_fixture, function_fixture):

    """This test checks concatenation of strings."""

    str1 = 'abc'
    str2 = 'def'
    assert str1 + str2 == 'abcdef', "Concatenation doesn't work."


def test_addition(session_fixture, module_fixture, function_fixture):

    """This test checks addition of integers."""

    a = b = 2
    assert a + b == 4, "Addition doesn't work."


def test_subtraction(session_fixture, module_fixture, function_fixture):

    """This test checks subtraction of integers."""

    a = b = 2
    assert a - b == 0, "Subtraction doesn't work."


def test_multiplying(session_fixture, module_fixture, function_fixture):

    """This test checks multiplying of integers."""

    a = b = 2
    assert a * b == 4, "Multiplying doesn't work."


def test_division(session_fixture, module_fixture, function_fixture):

    """This test checks division of integers."""

    a = b = 2
    assert a / b == 1, "Division doesn't work."
