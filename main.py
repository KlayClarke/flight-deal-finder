from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

fs = FlightSearch()
fd = FlightData()
dm = DataManager()
nm = NotificationManager()

city_data = dm.read_rows()


# if price is less than our lowest price listed in google sheets, sens sms
for city in city_data:
    cheapest_flight_info = fd.find_flight_info(city_code=city['iataCode'], max_price=city['lowestPrice'])
    try:
        city_name = (cheapest_flight_info['data'][0]['cityTo'])
        nights_in_destination = (cheapest_flight_info['data'][0]['nightsInDest'])
        flight_price = (cheapest_flight_info['data'][0]['price'])
        link_to_deal = (cheapest_flight_info['data'][0]['deep_link'])
    except IndexError:
        pass
    else:
        sms_text = f'Low price alert! Only ${flight_price} to fly from Boston ' \
                   f'and spend {nights_in_destination} days in {city_name}\n' \
                   f'Link: {link_to_deal}'
        nm.send_sms(sms_text=sms_text)

# # populate iata codes for each entry in google sheet if they are empty
# for city in city_data:
#     if city['iataCode'] == '':
#         print(dm.update_iata_codes(city_code=fs.find_city_code(city['city']), id=city['id']))

# # if flight price is less than our lowest price listed in google sheets, print price in console
# for city in city_data:
#     cheapest_flight_info = (fd.find_flight_info(city_code=city['iataCode'],max_price=city['lowestPrice']))
#     try:
#         city_name = (cheapest_flight_info['data'][0]['cityTo'])
#         nights_in_destination = (cheapest_flight_info['data'][0]['nightsInDest'])
#         flight_price = (cheapest_flight_info['data'][0]['price'])
#         link_to_deal = (cheapest_flight_info['data'][0]['deep_link'])
#         print(f'${flight_price}\n{nights_in_destination} nights in {city_name}\nLink: {link_to_deal} ')
#     except IndexError:
#         pass
