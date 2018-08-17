from unittest.mock import MagicMock
from tz_pyramid.ui.tests.abc.MyAbc import AbstractAdder, ConcreteAdder, AddExecuter

def test_canCallAddExecuter():
    print("===================110")
    adder = ConcreteAdder()
    AddExecuter(adder)
    print("===================111")

def test_AddExecuterCallAddAndReturnsResult():
    print("===================220")
    mock_adder = MagicMock(AbstractAdder)
    mock_adder.add = MagicMock(return_value=3)
    result = AddExecuter(mock_adder)
    mock_adder.add.assert_called_once_with(1, 2)
    print("===================222")
    assert result == 3