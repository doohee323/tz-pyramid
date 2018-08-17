import pytest
from pytest import raises
from tz_pyramid.ui.tests.test_setup1 import raiseValueException


@pytest.mark.test41
def test4():
    print("Executing test4")
    with raises(ValueError):
        raiseValueException(1)
        #raiseValueException(2)

@pytest.mark.test5
def test5():
    print("Executing test5")
    with raises(ValueError):
        raiseValueException(1)
