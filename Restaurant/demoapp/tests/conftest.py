
import os
import sys
from flask import url_for, request
from demoapp import (create_app)
import pytest


""" Fixtures for different test clients (different browsers) """


@pytest.fixture(scope='session')
def test_client():
    """ Create the application and the test client.
    The way a fixture works is whaterver is yielded
    by this function will be passed to the tests that 
    take the name of the fixture function as an argument.
    """
    print('----------Setup test client----------')

    app = create_app()
    app.config["WTF_CSRF_ENABLED"] = False
    # testing_client = app.test_client()
    testing_client = app.test_client()

    # makes it so I can use the url_for() function in the tests
    ctx = app.test_request_context()
    ctx.push()
    yield testing_client  # this is where the testing happens
    print('-------Teardown test client--------')

    ctx.pop()
