import requests
import pprint

api_key = "EV1V34XV7I79WDYJ"

API_URL = "https://www.alphavantage.co/query"


def time_series_request_adjusted(symbol):
    global api_key
    data = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": api_key,
    }
    response = requests.get(API_URL, data)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response.json())


time_series_request_adjusted("GOOG")
