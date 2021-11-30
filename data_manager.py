import os
import requests

SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')

sheety_header = {
    'Authorization': SHEETY_API_KEY
}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_codes = {}

    def read_rows(self):
        sheety_response = requests.get(url=SHEETY_ENDPOINT)
        sheety_response.raise_for_status()
        sheety_data = sheety_response.json()
        self.destination_codes = sheety_data['prices']
        return self.destination_codes

    def add_row(self, city_name, iata_code, lowest_price):
        sheety_params = {
            'price': {
                'city': city_name,
                'iataCode': iata_code,
                'lowestPrice': lowest_price
            }
        }
        sheety_response = requests.request('POST', url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_header)
        sheety_response.raise_for_status()
        sheety_data = sheety_response.json()
        return sheety_data

    def update_row(self, row_id, city_name, iata_code, lowest_price):
        sheety_params = {
            'price': {
                'city': city_name,
                'iataCode': iata_code,
                'lowestPrice': lowest_price
            }
        }
        sheety_endpoint = f'{SHEETY_ENDPOINT}{row_id}'
        sheety_response = requests.put(url=sheety_endpoint, json=sheety_params, headers=sheety_header)
        sheety_response.raise_for_status()
        sheety_data = sheety_response.json()
        return sheety_data

    def delete_row(self, row_num):
        sheety_endpoint = f'{SHEETY_ENDPOINT}{row_num}'
        sheety_delete = requests.delete(url=sheety_endpoint)
        sheety_delete.raise_for_status()
        sheety_data = sheety_delete.json()
        return sheety_data


