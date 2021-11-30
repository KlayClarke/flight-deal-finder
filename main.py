# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import requests

import flight_search as fs

tequila_response = requests.get(url=fs.tequila_endpoint, params=fs.tequila_params, headers=fs.tequila_header)
tequila_response.raise_for_status()
flight_search_data = tequila_response.json()
print(flight_search_data)

