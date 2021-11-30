from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

fs = FlightSearch()
fd = FlightData()
dm = DataManager()

city_data = dm.read_rows()

# if flight price is less that our lowest price listed in google sheets, print price in console
for city in city_data:
    cheapest_flight_info = (fd.find_flight_info(city_code=city['iataCode'],max_price=city['lowestPrice']))
    try:
        city_name = (cheapest_flight_info['data'][0]['cityTo'])
        flight_price = (cheapest_flight_info['data'][0]['price'])
        link_to_deal = (cheapest_flight_info['data'][0]['deep_link'])
        print(f'{city_name}: £{flight_price}\nLink: {link_to_deal} ')
    except IndexError:
        pass
