import requests


def get_api_key() -> str:
    return open('api_key', 'r').read()


def build_url(key: str, location: str, days: str) -> str:
    return f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days={days}&aqi=yes&alerts=no"


def get_weather(url: str):
    return requests.get(url).json()


def show_current(location: str):
    url = build_url(get_api_key(), location, 1)
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
    url = build_url(get_api_key(), location, 1)
    data = get_weather(url)
    curr = {'name': data['location']['name'], 'condition': data['current']['condition']['text']}
    for key in ['temp_c', 'temp_f', 'wind_mph', 'pressure_mb', 'precip_in', 'humidity', 'cloud', 'uv']:
        curr[key] = data['current'][key]
    return curr


def show_forecast(location: str, days: str):
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
