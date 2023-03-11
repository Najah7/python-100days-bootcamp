"""
Project Lowest Price Notify!! (Flight version)
"""

# HACK:日本円対応機能を追加して

from datetime import datetime, timedelta
import requests 
import os 


# for dev 
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# load Environment variables
from dotenv import load_dotenv
load_dotenv()


SHEET_ENDPOINT = os.getenv('SHEET_ENDPOINT')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')

ORIGINAL_CITY_IATA = 'HND'

def main():
    
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager
    
    destinations_in_sheet = data_manager.fetch_destinations()
    
    if destinations_in_sheet[0]['iataCode'] == "":
        for row in destinations_in_sheet:
            row['iataCode'] = flight_search.fetch_destination_code(row['city'])
        data_manager.destination_data = destinations_in_sheet
        data_manager.update_destination_codes()
    
    tommorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
    
    for destination in destinations_in_sheet:
        flight = flight_search.check_flights(
            ORIGINAL_CITY_IATA,
            destination['iataCode'],
            from_time=tommorrow,
            to_time=six_month_from_today
        )
    
    if flight.price < destination['lowestPrice']:
        message = f"Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        notification_manager.send_email(message)
    
    
    



if __name__ == '__main__':
    main()