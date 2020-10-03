import company_dict
from api_requests import time_series_request_adjusted
import pprint

companies = company_dict.return_company_dictionary()

data = [
    ('SAP', 15),
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
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data_points)


if __name__ == '__main__':
    build_fond(data)
