# forecast-weather
This python library easily obtains weather data across various locations and dates.

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![](https://img.shields.io/github/issues/e7kim/forecast-weather)](https://github.com/e7kim/forecast-weather/issues)
[![Build Status](https://github.com/e7kim/forecast-weather/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/e7kim/forecast-weather/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/e7kim/forecast-weather/branch/main/graph/badge.svg)](https://codecov.io/gh/e7kim/forecast-weather)
[![PyPI](https://img.shields.io/pypi/v/forecast-weather)](https://pypi.org/project/forecast-weather/)

# Overview
`forecast-weather` is a library that allows a user to easily obtain weather data (temperatures, pressure, humidity, precipitation, wind, cloud coverage, etc.) across various locations and dates. The library will make calls to a public weather API and will organize the returned data for ease of use. Some extra functionality in consideration include some form of visual plot/graph generation.

## Install
```
pip install forecast-weather
```

## API Key
Go to [weatherapi.com](https://www.weatherapi.com/) to register an account for your free api key. Create a new file **./api_key** and paste your api key here.

## Usage
```
import forecast_weather as fw

fw.show_current(location = "10027")
fw.show_forecast(location = "10027", days = "2")
current = fw.get_current(location = "10027")
forecast = fw.get_forecast(location = "10027", days = "3")
```

## Details
This project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:
- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution