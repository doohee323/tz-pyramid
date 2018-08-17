import pytest
from pytest import approx, raises


@pytest.fixture() # autouse=True
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture(params=[4,3,1])
def setup2(request):
    print("\nSetup2")
    retVal = request.param
    print("\nSetup2 retVal = {}".format(retVal))

    def teartdown_a():
        print("\nTeardown A")

    def teartdown_b():
        print("\nTeardown B")

    request.addfinalizer(teartdown_a)
    request.addfinalizer(teartdown_b)

    return retVal


def test1(setup1):
    print("Executing test1")
    assert (0.1 + 0.2) == approx(0.3)

def test2(setup2):
    print("Executing test2 {}".format(setup2))
    assert True

def raiseValueException(arg):
    print("raiseValueException is called " + str(arg))
    if arg == 1:
        raise ValueError
    else:
        pass

def test3():
    print("Executing test3")
    with raises(ValueError):
        raiseValueException(1)
    print("Executing test3-1")
    # with raises(ValueError):
    #     raiseValueException(2)

