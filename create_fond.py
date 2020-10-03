import company_dict
from api_requests import time_series_request_adjusted
import pprint

companies = company_dict.return_company_dictionary()

data = [
    ('SAP', 80),
    ('IBM', 20),
]


def build_fond(data):
    companies = []
    i = 0
    for x in data:
        companies.append(data[i][0])
        i += 1
    data_points = {}
    for company in companies:
        response = time_series_request_adjusted(company)
        data_points.update({company: []})
        for key in response['Time Series (Daily)']:
            close = response['Time Series (Daily)'][key]['4. close']
            # for understanding: key equals a date here; create a tupel of a date and a price
            data_point = (key, close)
            data_points[company].append(data_point)
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(data_points)
    return data_points


def norm_fond(data_points, data):
    """
    This function normalizes the given assets
    """

    # pick the latest values of each asset
    latest_values = []
    for asset in data:
        asset_symbol = asset[0]
        latest_values.append((asset_symbol, data_points[asset_symbol][0][1], asset[1]))

    # Creating a list of tuples (percentage from given portfolio, stock_price)
    factor_list = {}
    for x in latest_values:
        symbol = x[0]
        stock_price = float(x[1])
        percentage = float(x[2])
        factor_list.update({symbol: percentage / stock_price})

    # multiplying given asset prices with multiplyer
    normalized_data_points = {}
    for asset in data:
        asset_symbol = asset[0]
        factor = factor_list[asset_symbol]
        normalized_data_points.update({asset_symbol: []})
        for data_point in data_points[asset_symbol]:
            normalized_data_point = factor * float(data_point[1])
            normalized_data_points[asset_symbol].append((data_point[0], normalized_data_point))

    return normalized_data_points


if __name__ == '__main__':
    data_points = build_fond(data)
    norm_fond(data_points, data)
