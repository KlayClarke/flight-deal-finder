import os
import requests
import datetime
from flight_search import tequila_header

TEQUILA_FLIGHT_SEARCH_ENDPOINT = os.environ.get('TEQUILA_FLIGHT_SEARCH_ENDPOINT')

tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
in_two_months = (datetime.date.today() + datetime.timedelta(days=60)).strftime('%d/%m/%Y')


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        pass

    # flight prices from London to destination
    def find_flight_info(self, city_code, max_price):
        tequila_params = {
            'fly_from': 'LON',
            'fly_to': city_code,
            'date_from': tomorrow,
            'date_to': in_two_months,
            'price_from': 0,
            'price_to': max_price,
            'curr': 'GBP',
            'max_stopovers': 0,
            'limit': 1
        }
        tequila_response = requests.get(url=TEQUILA_FLIGHT_SEARCH_ENDPOINT,
                                        params=tequila_params,
                                        headers=tequila_header)
        tequila_response.raise_for_status()
        tequila_data = tequila_response.json()
        return tequila_data
