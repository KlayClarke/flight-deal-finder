from data_manager import DataManager
from flight_search import FlightSearch

fs = FlightSearch()
dm = DataManager()

# # Attempt to read spreadsheet and update the iata code on each row
for city in dm.read_rows():
    city_name = city['city']
    code = (fs.city_code(city_name))
    lowest_price = city['lowestPrice']
    row_id = city['id']
    dm.update_row(row_id=row_id, city_name=city_name, iata_code=code, lowest_price=lowest_price)
