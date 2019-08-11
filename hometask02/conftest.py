# -*- coding: UTF-8 -*-

"""Fixtures."""

import pytest


@pytest.fixture(scope='session')
def session_fixture():

    """Shows boundaries of session."""

    print("\nStart of session.")

    yield

    print("\nEnd of session.")


@pytest.fixture(scope='module')
def module_fixture():

    """Shows boundaries of module."""

    print("\nStart of module.")

    yield

    print("\nEnd of module.")


@pytest.fixture
def function_fixture():

    """Shows boundaries of function."""

    print("\nStart of function.")

    yield

    print("\nEnd of function.")
