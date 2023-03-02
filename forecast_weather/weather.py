import requests
import datetime as dt

def hello() -> str:
    return "Hello, world!"

def print_hello() -> None:
    print(hello())

def get_api_key() -> str:
    return open('api_key', 'r').read()

def build_url(lat: str, lon: str, part: str, key: str) -> str:
    return f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}"

def get_weather(lat: str, lon: str, part: str):
    url = build_url(lat, lon, part, get_api_key())
    return requests.get(url).json()

def kelvin_to_fahrenheit(temp: int) -> int:
    return 9/5 * (temp - 273.15) + 32

def show_current(lat: str, lon: str, part: str):
    resp = get_weather(lat, lon, part)
    temp = kelvin_to_fahrenheit(resp['current']['temp'])
    feels_like = kelvin_to_fahrenheit(resp['current']['feels_like'])
    pressure = resp['current']['feels_like']
    humidity = resp['current']['humidity']
    dew_point = resp['current']['dew_point']
    uvi = resp['current']['uvi']
    clouds = resp['current']['clouds']
    wind_speed = resp['current']['wind_speed']

    print(f"Current weather at ({lat}, {lon}) is: ")
    print(f"Temperature: {temp}")
    print(f"Temperature feels like: {feels_like}")
    print(f"Pressure: {pressure} mbar")
    print(f"Humidity: {humidity}%")
    print(f"Dew Point: {dew_point}")
    print(f"UVI: {uvi}")
    print(f"Cloud coverage: {clouds}%")
    print(f"Wind speed: {wind_speed}")