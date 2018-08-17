import pytest

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup session")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup module")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup function")

def test1():
    print("test1")
    assert True

def test2():
    print("test2")
    assert True

