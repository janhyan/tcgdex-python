import requests
from errors import NoCardsFound, NoSetsFound

BASE_URL = 'https://api.tcgdex.net/v2'
ENDPOINTS = ['name', 'categories', 'energy-types', 'hp',
             'illustrators', 'rarities', 'retreats',
             'stages', 'suffixes', 'trainer-types', 
             'dex-ids', 'types', 'series', 'sets']

class TCGDex:
    def __init__(self, lang='en'):
        self.lang = lang

    def _handle_response(self, response, not_found_exception):
        """Helper method to handle API responses."""
        if response.get('status') == 404:
            raise not_found_exception
        return response

    def fetch_card(self, card_id):
        """Fetch details of a single card by its ID."""
        response = requests.get(f'{BASE_URL}/{self.lang}/cards/{card_id}').json()
        try:
            return self._handle_response(response, NoCardsFound)
        except NoCardsFound:
            print(f"No card found with ID: {card_id}")

    def fetch_all_cards(self):
        """Fetch all available cards."""
        return requests.get(f'{BASE_URL}/{self.lang}/cards').json()

    def fetch_set(self, set_code):
        """Fetch details of a set by its code."""
        response = requests.get(f'{BASE_URL}/{self.lang}/sets/{set_code}').json()
        try:
            return self._handle_response(response, NoSetsFound)
        except NoSetsFound:
            print(f"No set found with code: {set_code}")

    def fetch_all_sets(self):
        """Fetch all available sets."""
        return requests.get(f'{BASE_URL}/{self.lang}/sets').json()

    def fetch_card_id(self, set_id, local_id):
        """Fetch a card by set ID and local ID."""
        response = requests.get(f'{BASE_URL}/{self.lang}/sets/{set_id}/{local_id}').json()
        try:
            return self._handle_response(response, NoCardsFound)
        except NoCardsFound:
            print(f"No card found with Set ID: {set_id} and Local ID: {local_id}")

    def fetch_serie(self, serie_id):
        """Fetch details of a series by its ID."""
        response = requests.get(f'{BASE_URL}/{self.lang}/series/{serie_id}').json()
        try:
            return self._handle_response(response, NoCardsFound)
        except NoCardsFound:
            print(f"No series found with ID: {serie_id}")

    def fetch_series(self):
        """Fetch all available series."""
        return requests.get(f'{BASE_URL}/{self.lang}/series').json()
    
    def fetch(self, endpoint, identifier):
        if endpoint not in ENDPOINTS:
            raise ValueError(f"Invalid endpoint: {endpoint}")

        # Construct URL based on the endpoint
        if endpoint in ['series', 'sets']:
            url = f"{BASE_URL}/{self.lang}/{endpoint}?name={identifier}"
        else:
            url = f"{BASE_URL}/{self.lang}/cards?{endpoint}={identifier}"

        response = requests.get(url).json()

        try:
            return response
        except NoCardsFound:
            print(f"No cards found with {endpoint}: {identifier}")

test = TCGDex('en')
print(test.fetch_set("swsh3"))