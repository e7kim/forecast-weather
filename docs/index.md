# Welcome to forecast-weather's documentation!

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


```eval_rst
.. autofunction:: forecast_weather.show_current
.. autofunction:: forecast_weather.get_current
.. autofunction:: forecast_weather.show_forecast
.. autofunction:: forecast_weather.get_forecast
```