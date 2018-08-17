from tz_pyramid.ui.tests.network.network_mock import getURL
from unittest.mock import MagicMock

def test_canCallGetURL():
    result = getURL("http://www.cnn.com")
    assert result.status_code == 200

def test_callGetAndReturnsGoodResult(monkeypatch):
    mock_result = MagicMock()
    mock_result.status_code = 200
    mock_get = MagicMock(return_value=mock_result)
    monkeypatch.setattr("requests.get", mock_get)
    result = getURL("http://www.cnn.com")
    mock_get.assert_called_once_with("http://www.cnn.com")
    assert result.status_code == 200


