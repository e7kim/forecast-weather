import requests


def get_api_key() -> str:
    return open('api_key', 'r').read()


def build_url(key: str, location: str, days: str) -> str:
    return f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days={days}&aqi=yes&alerts=no"


def get_weather(url: str):
    return requests.get(url).json()


def show_current(location: str):
    """Prints the current weather conditions at a given location.

    Args:
        location (str): Query for a location, could be a US Zipcode, UK Postcode, Canada Postalcode,
            IP address, Latitude/Longitude (decimal degree) or city name.

    Returns:
        None: See note for the printing side effect.

    Note:
        Prints the current temperature in Fahrenheit/Celsius, weather condition, wind speed, air pressure,
        precipitation, humidity, cloud coverage, and UV of the specified location.

    """
    url = build_url(get_api_key(), location, "1")
    data = get_weather(url)
    print(f"Current weather at {data['location']['name']} is: ")
    print(f"Temperature: {data['current']['temp_f']} F/ {data['current']['temp_c']} C")
    print(f"Condition: {data['current']['condition']['text']}")
    print(f"Wind speed: {data['current']['wind_mph']} mph")
    print(f"Pressure: {data['current']['pressure_mb']} mb")
    print(f"Precipitation: {data['current']['precip_in']} in")
    print(f"Humidity: {data['current']['humidity']}%")
    print(f"Cloud coverage: {data['current']['cloud']}%")
    print(f"UV: {data['current']['uv']}")


def get_current(location: str):
    """Returns the current weather conditions at a given location.

    Args:
        location (str): Query for a location, could be a US Zipcode, UK Postcode, Canada Postalcode,
            IP address, Latitude/Longitude (decimal degree) or city name.

    Returns:
        dict: A hash map containing the name of the location, current temperature in Fahrenheit/Celsius,
        weather condition, wind speed, air pressure, precipitation, humidity, cloud coverage, and UV of
        the specified location.

    Note:
        In regards to accessing the weather data from the returned dictionary, the relevant keys are name,
        condition, temp_c, temp_f, wind_mph, pressure_mb, precip_in, humidity, cloud, uv.

    """
    url = build_url(get_api_key(), location, "1")
    data = get_weather(url)
    curr = {'name': data['location']['name'], 'condition': data['current']['condition']['text']}
    for key in ['temp_c', 'temp_f', 'wind_mph', 'pressure_mb', 'precip_in', 'humidity', 'cloud', 'uv']:
        curr[key] = data['current'][key]
    return curr


def show_forecast(location: str, days: str):
    """Prints the forecast weather conditions at a given location across a given number of days.

    Args:
        location (str): Query for a location, could be a US Zipcode, UK Postcode, Canada Postalcode,
            IP address, Latitude/Longitude (decimal degree) or city name.
        days (str): Value from 1 to 10 that specifies the number of days to forecast. There may be
            tighter upper limits depending on the particular plan one's API key is from. See
            https://www.weatherapi.com/pricing.aspx for more information.

    Returns:
        None: See note for the printing side effect.

    Note:
        Prints the forecast average temperature in Fahrenheit/Celsius, weather condition, max wind speed,
        total precipitation, average humidity, and UV of the specified location across the time frame.

    """
    url = build_url(get_api_key(), location, days)
    data = get_weather(url)
    for i in range(len(data['forecast']['forecastday'])):
        print(f"{data['forecast']['forecastday'][i]['date']} weather forecast of {data['location']['name']} is: ")
        print(
            f"Average temperature: {data['forecast']['forecastday'][i]['day']['avgtemp_f']} F/ "
            + f"{data['forecast']['forecastday'][i]['day']['avgtemp_c']} C",
        )
        print(f"Condition: {data['forecast']['forecastday'][i]['day']['condition']['text']}")
        print(f"Max wind speed: {data['forecast']['forecastday'][i]['day']['maxwind_mph']} mph")
        print(f"Total precipitation: {data['forecast']['forecastday'][i]['day']['totalprecip_in']} in")
        print(f"Average humidity: {data['forecast']['forecastday'][i]['day']['avghumidity']}%")
        print(f"UV: {data['forecast']['forecastday'][i]['day']['uv']}")


def get_forecast(location: str, days: str):
    """Returns the forecast weather conditions at a given location.

    Args:
        location (str): Query for a location, could be a US Zipcode, UK Postcode, Canada Postalcode,
            IP address, Latitude/Longitude (decimal degree) or city name.
        days (str): Value from 1 to 10 that specifies the number of days to forecast. There may be
            tighter upper limits depending on the particular plan one's API key is from. See
            https://www.weatherapi.com/pricing.aspx for more information.

    Returns:
        dict: A hash map containing the name of the location, forecast temperature in Fahrenheit/Celsius,
        weather condition, wind speed, air pressure, precipitation, humidity, cloud coverage, and UV of
        the specified location across the time frame.

    Note:
        In regards to accessing the weather data from the returned dictionary, the relevant keys are name
        and the dates in the format YYYY-MM-DD. The dates access a nested dictionary where the relevant
        keys are avgtemp_f, avgtemp_c, condition, maxwind_mph, totalprecip_in, avghumidity, and uv.

    """
    url = build_url(get_api_key(), location, days)
    data = get_weather(url)
    forecast = {'name': data['location']['name']}
    for i in range(len(data['forecast']['forecastday'])):
        day = {}
        day['avgtemp_f'] = data['forecast']['forecastday'][i]['day']['avgtemp_f']
        day['avgtemp_c'] = data['forecast']['forecastday'][i]['day']['avgtemp_c']
        day['condition'] = data['forecast']['forecastday'][i]['day']['condition']['text']
        day['maxwind_mph'] = data['forecast']['forecastday'][i]['day']['maxwind_mph']
        day['totalprecip_in'] = data['forecast']['forecastday'][i]['day']['totalprecip_in']
        day['avghumidity'] = data['forecast']['forecastday'][i]['day']['avghumidity']
        day['uv'] = data['forecast']['forecastday'][i]['day']['uv']
        forecast[data['forecast']['forecastday'][i]['date']] = day
    return forecast
