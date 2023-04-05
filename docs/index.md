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
```python
import forecast_weather as fw

fw.show_current(location = "10027")
fw.show_forecast(location = "10027", days = "2")
current = fw.get_current(location = "10027")
forecast = fw.get_forecast(location = "10027", days = "3")
```

## Examples
1. Running the following code
    ```python
    import forecast_weather as fw

    fw.show_current(location = "10027")
    ```
    Outputs something like this to the console
    ```
    Current weather at New York is: 
    Temperature: 68.0 F/ 20.0 C
    Condition: Overcast
    Wind speed: 2.2 mph
    Pressure: 1017.0 mb
    Precipitation: 0.0 in
    Humidity: 55%
    Cloud coverage: 100%
    UV: 4.0
    ```
2. Running the following code
    ```python
    import forecast_weather as fw

    d = fw.get_current(location = "10027")
    ```
    Saves a dictionary like
    ```
    {
        'name': 'New York', 
        'condition': 'Clear',
        'temp_c': 17.8,
        'temp_f': 64.0,
        'wind_mph': 2.2,
        'pressure_mb': 1019.0,
        'precip_in': 0.0,
        'humidity': 73,
        'cloud': 0,
        'uv': 1.0
    }
    ```
3. Running the following code
    ```python
    import forecast_weather as fw

    fw.show_forecast(location = "10027", days = "2")
    ```
    Outputs something like this to the console
    ```
    2023-04-04 weather forecast of New York is: 
    Average temperature: 55.7 F/ 13.2 C
    Condition: Cloudy
    Max wind speed: 8.3 mph
    Total precipitation: 0.0 in
    Average humidity: 84.0%
    UV: 3.0
    2023-04-05 weather forecast of New York is: 
    Average temperature: 51.0 F/ 10.6 C
    Condition: Overcast
    Max wind speed: 12.5 mph
    Total precipitation: 0.0 in
    Average humidity: 92.0%
    UV: 3.0
    ```
4. Running the following code
    ```python
    import forecast_weather as fw

    d = fw.get_forecast(location = "10027", days = "2")
    ```
    Saves a dictionary like
    ```
    {
        'name': 'New York',
        '2023-04-04': {
            'avgtemp_f': 55.7,
            'avgtemp_c': 13.2,
            'condition': 'Cloudy',
            'maxwind_mph': 8.3,
            'totalprecip_in': 0.0,
            'avghumidity': 84.0,
            'uv': 3.0
        },
        '2023-04-05': {
            'avgtemp_f': 51.0,
            'avgtemp_c': 10.6,
            'condition': 'Overcast',
            'maxwind_mph': 12.5,
            'totalprecip_in': 0.0,
            'avghumidity': 92.0,
            'uv': 3.0
        }
    }
    ```

## Demo

![](https://raw.githubusercontent.com/e7kim/forecast-weather/main/docs/img/demo.gif)

## API Documentation
```eval_rst
.. toctree::
   :maxdepth: 2

   source/forecast_weather
```