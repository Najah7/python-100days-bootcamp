import requests 
import os 

# for dev 
from pprint import pprint

# load Environment variables
from dotenv import load_dotenv
load_dotenv()

SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self) -> None:
        self.destination_data = {}
        self.sheet_endpoint = os.getenv('SHEET_ENDPOINT')
    
    def fetch_destinations(self):
        res = requests.get(
            self.sheet_endpoint,
            headers={'Authorization': SHEETY_TOKEN}
            )
        
        self.destination_data = res.json()['prices']
        return self.destination_data
    
    def update_destination_codes(self):
        
        for city in self.destination_data:
            new_data = {
                'price': {
                    "iataCode": city['iataCode']
                }
            }
            res = requests.put(
                f"{self.sheet_endpoint}/{city['id']}",
                json=new_data
                )
            # for logging
            print(res.text)
        
    
    # HACK:このクラスにいれる？
    def params_to_update_iata_code(self, code):
        params = {
            'price': {
                'iataCode': code
            }
        }
        
        return params