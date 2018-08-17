import pytest
from unittest.mock import MagicMock
from tz_pyramid.ui.views.RESTView import RESTView

@pytest.fixture()
def testapp():
    from tz_pyramid import main
    app = main({})
    from webtest import TestApp
    testapp = TestApp(app)
    return testapp

def test_canCalculateTotal(testapp):
    rest = RESTView('/')
    rest.get()
    # testapp.addItem("a")
    # assert testapp.calculateTotal() == 1
