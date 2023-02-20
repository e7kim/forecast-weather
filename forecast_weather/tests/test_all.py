from forecast_weather import *
from unittest.mock import patch


def test_hello():
    assert hello() == "Hello, world!"


@patch('builtins.print')
def test_print_hello(mock_print):
    print_hello()
    assert mock_print.call_args.args == ("Hello, world!",)

def test_get_api_key():
    assert get_api_key() == open('api_key', 'r').read()