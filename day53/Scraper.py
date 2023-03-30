import os
import requests

from bs4 import BeautifulSoup

import dotenv
dotenv.load_dotenv()

ZILLOW_URL = os.getenv('ZILLOW_URL')

class Scraper:
    def __init__(self, url) -> None:
        self.url = url
        self.soup = BeautifulSoup(self._fetch_data(), 'html.parser')
        
        
    
    def _fetch_data(self):
        return requests.get(self.url).text
    
    def print_data(self):
        print(self.soup.text)
    
    


class SfRentalScraper(Scraper):
    def __init__(self) -> None:
        super().__init__(ZILLOW_URL)
        
    def get_address(self):
        return self.soup.find_all('address', {'class': 'property-card-addr'})
        
    def get_price(self):
        return self.soup.find_all('span', {'class': 'property-card-price'})
    
    def get_link(self):
        return self.soup.find_all('a', {'class': 'property-card-link'}).get('href')
        
scraper = SfRentalScraper()
print(scraper.print_data())