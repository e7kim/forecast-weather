import requests


def get_api_key() -> str:
    return open('api_key', 'r').read()


def build_url(key: str, location: str, days: str) -> str:
    return f"http://api.weatherapi.com/v1/forecast.json?key={key}&q={location}&days={days}&aqi=yes&alerts=no"


def get_weather(url: str):
    return requests.get(url).json()


def show_current(location: str, days: str):
    url = build_url(get_api_key(), location, days)
    data = get_weather(url)
    name = data['location']['name']
    temp_c = data['current']['temp_c']
    temp_f = data['current']['temp_f']
    condition = data['current']['condition']['text']
    wind_mph = data['current']['wind_mph']
    pressure = data['current']['pressure_mb']
    precip = data['current']['precip_in']
    humidity = data['current']['humidity']
    cloud = data['current']['cloud']
    uv = data['current']['uv']

    print(f"Current weather at {name} is: ")
    print(f"Temperature: {temp_f} F/ {temp_c} C")
    print(f"Condition: {condition}")
    print(f"Wind speed: {wind_mph} mph")
    print(f"Pressure: {pressure} mb")
    print(f"Precipitation: {precip} in")
    print(f"Humidity: {humidity}%")
    print(f"Cloud coverage: {cloud}%")
    print(f"UV: {uv}")
