"""
Project Weather Notification

This is for API(with Authentication) and Sending SMS
"""

"""
twilio
クラウドコミュニケーションプラットフォームサービス
電話の発着信やテキストメッセージの送受信をはじめ、その他の様々な通信機能をソフトウェアをAPIとして公開している
"""


import requests
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
MY_LAT = os.getenv('MY_LAT')
MY_LONG = os.getenv('MY_LONG')

OWM_ENDPONT = "https://api.openweathermap.org/data/3.0/onecall"


params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'exclude': 'current,minutely,daily',
    'appid': API_KEY,
}

res = requests.get(OWM_ENDPONT, params)
res.raise_for_status()
weather_data = res.json()

# NOTE:OWM Condition IDs and Condition Codes:https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2

will_rain = False

hourly_weather = weather_data['hourly']
hourly_weather_next_12 = hourly_weather[:12]

for hour_weather in hourly_weather_next_12:
    condition_code = hour_weather['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella.")
    
    
"""
TWilioの電話番号認証が上手くいかずSMSメール断念。下記にTWilioのサンプルコードを記載
"""

"""
from twillo.rest import Client

api_key = < api key>
account_sid = < account_sid >
auth_token = < auth_token >

client = Client(account_sid, auth_token)
message = client.message.create(
    body='sampel message',
    from='< phone number you can get from Twilio console >'
    to='<phone number you wanna to mesaage>'
)

# you can check status
print(message.staus)

---------python anywhereに上げる場合、Proxyのためのコードが必要👇
from os
from twillo.rest import Client
from twilio.http.http_client import TwilioHttpClient
proxy_client = TwilioHttpClient(proxy={'hhtp': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

client = Client(account_sid, auth_token, http_client=proxy_client)
"""