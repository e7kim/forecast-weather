from forecast_weather import *
from unittest.mock import patch, mock_open, Mock, call


def test_get_api_key():
    with patch('builtins.open', mock_open(read_data="mock_key")) as mock_file:
        assert get_api_key() == "mock_key"
        mock_file.assert_called_with("api_key", "r")


def test_build_url():
    with patch('builtins.open', mock_open(read_data="mock_key")) as mock_file:
        assert (
            build_url(get_api_key(), "10027", "1")
            == f"http://api.weatherapi.com/v1/forecast.json?key=mock_key&q=10027&days=1&aqi=yes&alerts=no"
        )
        mock_file.assert_called_with("api_key", "r")


def test_get_weather_NYC_1day():
    with patch('builtins.open', mock_open(read_data="mock_key")) as mock_file:
        with patch('requests.get') as r_mock:
            r_mock.return_value = Mock(
                status_code=200,
                json=lambda: {"location": {"name": "New York"}, "forecast": {"forecastday": ["testday1"]}},
            )
            url = build_url(get_api_key(), "10027", "1")
            data = get_weather(url)
            assert data['location']['name'] == "New York"
            assert len(data['forecast']['forecastday']) == 1
            mock_file.assert_called_with("api_key", "r")


def test_get_weather_NYC_2days():
    with patch('builtins.open', mock_open(read_data="mock_key")) as mock_file:
        with patch('requests.get') as r_mock:
            r_mock.return_value = Mock(
                status_code=200,
                json=lambda: {"location": {"name": "New York"}, "forecast": {"forecastday": ["testday", "testday2"]}},
            )
            url = build_url(get_api_key(), "10027", "2")
            data = get_weather(url)
            assert data['location']['name'] == "New York"
            assert len(data['forecast']['forecastday']) == 2
            mock_file.assert_called_with("api_key", "r")


def test_get_weather_fails():
    with patch('builtins.open', mock_open(read_data="mock_key")) as mock_file:
        with patch('requests.get') as r_mock:
            r_mock.return_value = Mock(status_code=500, json=lambda: {})
            url = build_url(get_api_key(), "10027", "2")
            data = get_weather(url)
            assert data == {}


@patch('builtins.print')
def test_show_current_NYC(mock_print):
    with patch('builtins.open', mock_open(read_data="mock_key")) as mock_file:
        with patch('requests.get') as r_mock:
            r_mock.return_value = Mock(
                status_code=200,
                json=lambda: {
                    "location": {"name": "New York"},
                    "current": {
                        "temp_c": 6.7,
                        "temp_f": 44.1,
                        "condition": {"text": "Overcast"},
                        "wind_mph": 2.2,
                        "pressure_mb": 1021.0,
                        "precip_in": 30.14,
                        "humidity": 47,
                        "cloud": 100,
                        "uv": 3.0,
                    },
                },
            )
            url = build_url(get_api_key(), "10027", "2")
            data = get_weather(url)
            show_current("10027", "1")
            assert mock_print.mock_calls == [
                call("Current weather at New York is: "),
                call("Temperature: 44.1 F/ 6.7 C"),
                call("Condition: Overcast"),
                call("Wind speed: 2.2 mph"),
                call("Pressure: 1021.0 mb"),
                call("Precipitation: 30.14 in"),
                call("Humidity: 47%"),
                call("Cloud coverage: 100%"),
                call("UV: 3.0"),
            ]
