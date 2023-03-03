"""
Project ISS Overhead
"""

import requests
from datetime import datetime
import smtplib
import time

from .config import (
    MY_LAT,
    MY_LONG,
    TIME_DIFFERENCE,
    MY_EMAIL,
    PASSWORD
)
# ---------------------------- Main Logic ------------------------------- #
def main():
    iss_position = fetch_iss_position()
    sun_info = fetch_sun_info()
    now = datetime.now()
    sunrise_hour = sun_info['sunrise']
    sunset_hour = sun_info['sunset']
    if is_iss_overhead(iss_position[0], iss_position[1]) \
        and is_night(now.hour, sunrise=sunrise_hour, sunset=sunset_hour):
            send_email()

# ---------------------------- Funcs to Call API  ------------------------------- #
def fetch_iss_position():
    """Fetch the position of iss and return position tuple"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    iss_position = (iss_latitude, iss_longitude)
    
    return iss_position

   
def fetch_sun_info(): 
    """
    get sunset time and return sunrise and sunset time hour.
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    return {
        'sunrise': sunrise,
        'sunset': sunset,
    }

# ---------------------------- Funcs for this project ------------------------------- #

def is_iss_overhead(iss_latitude, iss_longitude):
    """Your position is within +5 or -5 degrees of the ISS position."""
    if MY_LAT -5 <= iss_latitude <= MY_LAT + 5 \
        and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
            return True
    return False


def is_night(now_hour, sunrise=5, sunset=19):
    """
    If the ISS is close to my current position
    and it is currently dark
    Then send me an email to tell me to look up.
    BONUS: run the code every 60 seconds.
    """
    japan_hour = now_hour + TIME_DIFFERENCE
    if 0 <= japan_hour <= sunrise \
        or sunset <= japan_hour <= 24:
            return True
    return False 

def send_email():
    """send email to myself"""
    contents = 'The ISS is above you in the sky.'
    
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:look up👆\n\n{contents}"
        )      


if __name__ == '__main__':
    while True:
        time.sleep(60)
        main()