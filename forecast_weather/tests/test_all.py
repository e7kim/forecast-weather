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
            url = build_url(get_api_key(), "10027", "1")
            data = get_weather(url)
            show_current("10027")
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


def test_get_current_NYC():
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
            url = build_url(get_api_key(), "10027", "1")
            data = get_weather(url)
            assert get_current("10027") == {
                "name": "New York",
                "temp_c": 6.7,
                "temp_f": 44.1,
                "condition": "Overcast",
                "wind_mph": 2.2,
                "pressure_mb": 1021.0,
                "precip_in": 30.14,
                "humidity": 47,
                "cloud": 100,
                "uv": 3.0,
            }


@patch('builtins.print')
def test_show_forecast_NYC(mock_print):
    with patch('builtins.open', mock_open(read_data="mock_key")) as mock_file:
        with patch('requests.get') as r_mock:
            r_mock.return_value = Mock(
                status_code=200,
                json=lambda: {
                    "location": {"name": "New York"},
                    "forecast": {
                        "forecastday": [
                            {
                                "date": "2023-04-03",
                                "date_epoch": 1680480000,
                                "day": {
                                    "maxtemp_c": 17.0,
                                    "maxtemp_f": 62.6,
                                    "mintemp_c": 2.7,
                                    "mintemp_f": 36.9,
                                    "avgtemp_c": 7.8,
                                    "avgtemp_f": 46.0,
                                    "maxwind_mph": 15.4,
                                    "maxwind_kph": 24.8,
                                    "totalprecip_mm": 0.0,
                                    "totalprecip_in": 0.0,
                                    "totalsnow_cm": 0.0,
                                    "avgvis_km": 10.0,
                                    "avgvis_miles": 6.0,
                                    "avghumidity": 63.0,
                                    "daily_will_it_rain": 0,
                                    "daily_chance_of_rain": 0,
                                    "daily_will_it_snow": 0,
                                    "daily_chance_of_snow": 0,
                                    "condition": {
                                        "text": "Partly cloudy",
                                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                                        "code": 1003,
                                    },
                                    "uv": 3.0,
                                },
                            },
                            {
                                "date": "2023-04-04",
                                "date_epoch": 1680566400,
                                "day": {
                                    "maxtemp_c": 19.1,
                                    "maxtemp_f": 66.4,
                                    "mintemp_c": 6.1,
                                    "mintemp_f": 43.0,
                                    "avgtemp_c": 13.1,
                                    "avgtemp_f": 55.5,
                                    "maxwind_mph": 8.7,
                                    "maxwind_kph": 14.0,
                                    "totalprecip_mm": 0.0,
                                    "totalprecip_in": 0.0,
                                    "totalsnow_cm": 0.0,
                                    "avgvis_km": 10.0,
                                    "avgvis_miles": 6.0,
                                    "avghumidity": 78.0,
                                    "daily_will_it_rain": 0,
                                    "daily_chance_of_rain": 0,
                                    "daily_will_it_snow": 0,
                                    "daily_chance_of_snow": 0,
                                    "condition": {
                                        "text": "Cloudy",
                                        "icon": "//cdn.weatherapi.com/weather/64x64/day/119.png",
                                        "code": 1006,
                                    },
                                    "uv": 3.0,
                                },
                            },
                        ]
                    },
                },
            )
            url = build_url(get_api_key(), "10027", "2")
            data = get_weather(url)
            show_forecast("10027", "2")
            assert mock_print.mock_calls == [
                call("2023-04-03 weather forecast of New York is: "),
                call("Average temperature: 46.0 F/ 7.8 C"),
                call("Condition: Partly cloudy"),
                call("Max wind speed: 15.4 mph"),
                call("Total precipitation: 0.0 in"),
                call("Average humidity: 63.0%"),
                call("UV: 3.0"),
                call("2023-04-04 weather forecast of New York is: "),
                call("Average temperature: 55.5 F/ 13.1 C"),
                call("Condition: Cloudy"),
                call("Max wind speed: 8.7 mph"),
                call("Total precipitation: 0.0 in"),
                call("Average humidity: 78.0%"),
                call("UV: 3.0"),
            ]


def test_get_forecast_NYC():
    with patch('builtins.open', mock_open(read_data="mock_key")) as mock_file:
        with patch('requests.get') as r_mock:
            r_mock.return_value = Mock(
                status_code=200,
                json=lambda: {
                    "location": {"name": "New York"},
                    "forecast": {
                        "forecastday": [
                            {
                                "date": "2023-04-03",
                                "date_epoch": 1680480000,
                                "day": {
                                    "maxtemp_c": 17.0,
                                    "maxtemp_f": 62.6,
                                    "mintemp_c": 2.7,
                                    "mintemp_f": 36.9,
                                    "avgtemp_c": 7.8,
                                    "avgtemp_f": 46.0,
                                    "maxwind_mph": 15.4,
                                    "maxwind_kph": 24.8,
                                    "totalprecip_mm": 0.0,
                                    "totalprecip_in": 0.0,
                                    "totalsnow_cm": 0.0,
                                    "avgvis_km": 10.0,
                                    "avgvis_miles": 6.0,
                                    "avghumidity": 63.0,
                                    "daily_will_it_rain": 0,
                                    "daily_chance_of_rain": 0,
                                    "daily_will_it_snow": 0,
                                    "daily_chance_of_snow": 0,
                                    "condition": {
                                        "text": "Partly cloudy",
                                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                                        "code": 1003,
                                    },
                                    "uv": 3.0,
                                },
                            },
                            {
                                "date": "2023-04-04",
                                "date_epoch": 1680566400,
                                "day": {
                                    "maxtemp_c": 19.1,
                                    "maxtemp_f": 66.4,
                                    "mintemp_c": 6.1,
                                    "mintemp_f": 43.0,
                                    "avgtemp_c": 13.1,
                                    "avgtemp_f": 55.5,
                                    "maxwind_mph": 8.7,
                                    "maxwind_kph": 14.0,
                                    "totalprecip_mm": 0.0,
                                    "totalprecip_in": 0.0,
                                    "totalsnow_cm": 0.0,
                                    "avgvis_km": 10.0,
                                    "avgvis_miles": 6.0,
                                    "avghumidity": 78.0,
                                    "daily_will_it_rain": 0,
                                    "daily_chance_of_rain": 0,
                                    "daily_will_it_snow": 0,
                                    "daily_chance_of_snow": 0,
                                    "condition": {
                                        "text": "Cloudy",
                                        "icon": "//cdn.weatherapi.com/weather/64x64/day/119.png",
                                        "code": 1006,
                                    },
                                    "uv": 3.0,
                                },
                            },
                        ]
                    },
                },
            )
            url = build_url(get_api_key(), "10027", "2")
            data = get_weather(url)
            assert get_forecast("10027", "2") == {
                'name': 'New York',
                '2023-04-03': {
                    'avgtemp_f': 46.0,
                    'avgtemp_c': 7.8,
                    'condition': "Partly cloudy",
                    'maxwind_mph': 15.4,
                    'totalprecip_in': 0.0,
                    'avghumidity': 63.0,
                    'uv': 3.0,
                },
                '2023-04-04': {
                    'avgtemp_f': 55.5,
                    'avgtemp_c': 13.1,
                    'condition': "Cloudy",
                    'maxwind_mph': 8.7,
                    'totalprecip_in': 0.0,
                    'avghumidity': 78.0,
                    'uv': 3.0,
                },
            }
