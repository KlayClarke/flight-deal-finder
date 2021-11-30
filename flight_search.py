import os

TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')

tequila_header = {
    'apikey': TEQUILA_API_KEY,
}

tequila_params = {
    'term': 'Paris'
}

tequila_endpoint = 'https://tequila-api.kiwi.com/locations/query'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass