import company_dict
import time_series_request_adjusted from api_requests
import pprint

companies = company_dict.return_company_dictionary()

data = [
    # ('SAP', 15),
    ('DAI', 35)
]


def test(data):
    company = data[0][0]
    print(company)
    response_json = time_series_request_adjusted(company)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response_json)


def build_fond(data):
    companies = data[0]
    data_points = []
    for company in companies:
        response_json = dict(api_requests.time_series_request_adjusted(company))
        data_points.append({company: []})
        # for key in response_json["Time Series (Daily)"]:
        #    close = response_json["Time Series (Daily"][key]["4. close"]
        #    # for understanding: key equals a date here; create a tupel of a date and a price
        #    data_point = (key, close)
        #    data_points[0][company].append(data_point)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(response_json["Time Series (Daily)"])
        print(data_points)


if __name__ == '__main__':
    test(data)
