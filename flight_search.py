import os
import requests

TEQUILA_ENDPOINT = os.environ.get('TEQUILA_ENDPOINT')
TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')

tequila_header = {
    'apikey': TEQUILA_API_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def find_city_code(self, city_name):
        tequila_params = {
            'term': city_name
        }
        tequila_response = requests.get(url=TEQUILA_ENDPOINT, params=tequila_params, headers=tequila_header)
        tequila_response.raise_for_status()
        tequila_data = tequila_response.json()
        city_data = tequila_data['locations'][0]
        city_code = city_data['code']
        return city_code
