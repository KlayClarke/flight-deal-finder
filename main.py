from data_manager import DataManager
from flight_search import FlightSearch

fs = FlightSearch()
dm = DataManager()
city_data = dm.read_rows()

for city in city_data:
    if city['iataCode'] == '':
        city_code = fs.find_city_code(city['city'])
        dm.update_iata_codes(city_code, city['id'])