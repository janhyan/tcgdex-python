import requests
import __main__

BASE_URL = 'https://api.tcgdex.net/v2'

class TCGDex:
    def __init__(self, lang= 'en') -> None:
        self.lang = lang

    def fetch_card(self, code):
        response = requests.get(f'{BASE_URL}/{self.lang}/cards/{code}')
        print(response.json())

test = TCGDex('en')
test.fetch_card()