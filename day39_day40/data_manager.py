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
        self.sheet_flight_endpoint = os.getenv('SHEET_FLIGHT_ENDPOINT')
        self.sheet_user_endpoint = os.getenv("SHEET_USER_ENDPOINT")
        self.headers={'Authorization': SHEETY_TOKEN}
    
    def fetch_destinations(self):
        res = requests.get(
            self.sheet_flight_endpoint,
            headers=self.headers
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
                f"{self.sheet_flight_endpoint}/{city['id']}",
                json=new_data,
                headers=self.headers,
                )
            # for logging
            print(res.text)
            
    def fetch_users(self):
        res = requests.get(self.sheet_user_endpoint)
        
        return res.json()
            
    def add_user(self, first_name, last_name, email):
        
        new_data = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email,
            }
        }
        res = requests.post(
            self.sheet_user_endpoint,
            json=new_data,
            headers=self.headers
        )
        
        res.raise_for_status()
        
        return res.json()
    
        
        
    
    # HACK:このクラスにいれる？
    def params_to_update_iata_code(self, code):
        params = {
            'price': {
                'iataCode': code
            }
        }
        
        return params
    
    