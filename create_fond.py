import company_dict
from api_requests import time_series_request_adjusted
import pprint

companies = company_dict.return_company_dictionary()

data = [
    # ('SAP', 15),
    ('DAI', 35)
]


#def test(data):
 #   company = data[0][0]
  #  print(company)
   # response_json = time_series_request_adjusted(company)
    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(response_json)


def build_fond(data):
    companies = data[0][0]
    data_points = {}
    for company in companies:
        response = time_series_request_adjusted(company)
        data_points.update({company: []})
        for key in response['Time Series (Daily)']:
            close = response['Time Series (Daily'][key]['4. close']
            # for understanding: key equals a date here; create a tupel of a date and a price
            data_point = (key, close)
            data_points[company].append(data_point)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data_points)


if __name__ == '__main__':
    build_fond(data)
