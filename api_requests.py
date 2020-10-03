import requests
import pprint
import json

api_key = "TREKF7IPFSYM0BGB"

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
    json_data = json.loads(response.text)
    return json_data
    #print(type(json_data))
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(json_data)


if __name__ == '__main__':
    time_series_request_adjusted("GOOG")
