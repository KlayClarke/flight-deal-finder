import os
import requests

SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')

sheety_header = {
    'Authorization': SHEETY_API_KEY
}

class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def read_rows(self):
        sheety_endpoint = 'https://api.sheety.co/7eaf685bcbfb9d696135db8f6a44daad/flightDeals/prices/'
        sheety_response = requests.get(url=sheety_endpoint)
        sheety_response.raise_for_status()
        sheety_data = sheety_response.json()
        sheety_cities = sheety_data['prices']
        return sheety_cities

    def add_row(self, city_name, iata_code, lowest_price):
        sheety_params = {
            'price': {
                'city': city_name,
                'iataCode': iata_code,
                'lowestPrice': lowest_price
            }
        }
        sheety_endpoint = 'https://api.sheety.co/7eaf685bcbfb9d696135db8f6a44daad/flightDeals/prices'
        sheety_response = requests.request('POST', url=sheety_endpoint, json=sheety_params, headers=sheety_header)
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
        sheety_endpoint = f'https://api.sheety.co/7eaf685bcbfb9d696135db8f6a44daad/flightDeals/prices/{row_id}'
        sheety_response = requests.put(url=sheety_endpoint, json=sheety_params, headers=sheety_header)
        sheety_response.raise_for_status()
        sheety_data = sheety_response.json()
        return sheety_data

    def delete_row(self, row_num):
        sheety_endpoint = f'https://api.sheety.co/7eaf685bcbfb9d696135db8f6a44daad/flightDeals/prices/{row_num}'
        sheety_delete = requests.delete(url=sheety_endpoint)
        sheety_delete.raise_for_status()
        sheety_data = sheety_delete.json()
        return sheety_data


