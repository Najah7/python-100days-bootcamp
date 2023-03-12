import requests
import os

# for dev
from pprint import pprint

from flight_data import FlightData



# load Environment variables
from dotenv import load_dotenv
load_dotenv()

TEQULIA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQULIA_API_KEY = os.getenv('TEQULIA_API_KEY')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def fetch_destination_code(self, city_name):
        location_endpoint = f"{TEQULIA_ENDPOINT}/locations/query"
        headers = {'apikey': TEQULIA_API_KEY}
        query = {"term": city_name, "location": "city"}
        res = requests.get(url=location_endpoint, headers=headers, params=query)
        result = res.json()['locations']
        code = result[0]['code']
        return code
    
    def check_flights(self,
                      origin_city_code,
                      destination_city_code,
                      from_time,
                      to_time
                      ):
        headers = {'apikey': TEQULIA_API_KEY}
        query = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime("%d/%m/%Y"),
            'date_to': to_time.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'one_for_city': 1,
            'max_stopover': 0,
            'cuur': 'GBP'
        }
        
        res = requests.get(
            f"{TEQULIA_ENDPOINT}/v2/search",
            headers=headers,
            params=query
        )
        res.raise_for_status()
        
        try:
            data = res.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")

            query["max_stopover"] = 1
            res = requests.get(
                f"{TEQULIA_ENDPOINT}/v2/search",
                headers=headers,
                params=query
            )
            
            data = res.json()['data'][0]
            pprint(data)
            flight_data = FlightData(
                price=data['price'],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]['cityTo']
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            
            return flight_data
        
        
        # HACK:日本円に換算する処理を追加（API探して）
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data