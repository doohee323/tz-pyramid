import pytest
from pytest import raises
from unittest.mock import MagicMock
from tz_pyramid.ui.tests.readfile.LineReader import readFromFile

@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.__enter__.return_value.__iter__.return_value = ["test line"]
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open

def test_retrunsCorrectString(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)

    monkeypatch.setattr("builtins.open", mock_open)
    result = readFromFile("blar")
    mock_open.assert_called_once_with("blar")
    assert result == "test line"


def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        readFromFile("blar")
