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

ORIGIN_CITY_IATA = 'HND'

def main():
    
    # make instances
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    
    print("Welcome to CLI Flight Club")
    
    is_same_password = False
    
    while not is_same_password:
    # user input
        first_name = input("What's your first name?\n")
        last_name = input("What's your last name?\n")
        email = input("What's your email?\n")
        confirm_email = input("Type your email again\n")
        
        if not email == confirm_email:
            continue
        
        is_same_password = True
    
    res = data_manager.add_user(first_name, last_name, email)
    
    pprint(res)
    
    destinations_in_sheet = data_manager.fetch_destinations()
    
    if destinations_in_sheet[0]['iataCode'] == "":
        for row in destinations_in_sheet:
            row['iataCode'] = flight_search.fetch_destination_code(row['city'])
        data_manager.destination_data = destinations_in_sheet
        data_manager.update_destination_codes()
    
    destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in destinations_in_sheet
    }
    
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
    
    for destination_code in destinations:
        flight = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination_code,
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        
        print(flight)
        
        if flight is None:
            continue
    
        if flight.price < destinations[destination_code]["price"]:
            users = data_manager.fetch_users()
            emails = [user['email'] for user in users]
            names = [user['firstName'] for user in users]
            message = f"Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            notification_manager.send_emails(emails, message)
    
if __name__ == '__main__':
    main()