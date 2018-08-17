import pytest

@pytest.fixture(scope = "session")
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture(scope = "session")
def setup2(request):
    print("\nSetup2")

    def teartdown_a():
        print("\nTeardown A")

    def teartdown_b():
        print("\nTeardown B")

    request.addfinalizer(teartdown_a)
    request.addfinalizer(teartdown_b)

@pytest.mark.usefixtures("setup1", "setup2")
def test1():
    pass

def method1(arg):
    print("Executing test1 arg:" + str(arg))
    assert True

def method2(arg):
    print("Executing test2")
    if arg == 1:
        return True
    else:
        raise ValueError('error!')

