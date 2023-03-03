"""
This Lecture is for API
"""

# NOTE:pythonでAPIを扱うときは、基本的にrequestsを使う

import requests
from requests import Response
from datetime import datetime

# NOTE:自分の地元の長崎の座標
MY_LAT = 32.750286
MY_LOG = 129.877670

"""
Status Code
・1XX：Hold on
・2XX：Here You Go
・3XX：Go Away
・4XX：You Screwed Up
・5XX：I Screwed Up
"""

# res = requests.get(url='http://api.open-notify.org/iss-now.json')
# res.raise_for_status() # 200以外の場合、それに適したエラーをraiseしてくれる。
# print(res.status_code)
# print(res.text)
# print(res.content)

# data = res.json()
# print(data)

# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']

# iss_position = (longitude, latitude)

"""
API Parameters
NOTE: APIの引数。関数の引数と同様に、parmeterを使うことでAPIの挙動を動的にできる。
NOTE: 基本的に「?param_name=value&param_name2=value2」で指定していする
"""

params = {
    'lat': MY_LAT,
    'log': MY_LOG,
    'formatted': 0,
}

res = requests.get('https://api.sunrise-sunset.org/json', params=params)
res.raise_for_status()
res_json = res.json()

sunrise = res_json['results']['sunrise']
sunset = res_json['results']['sunset']

def convert_to_time_list(date_with_default_format):
    return date_with_default_format.split('T')[1].split(':')

formatted_sunrise = convert_to_time_list(sunrise)
formatted_sunset = convert_to_time_list(sunset)
print(formatted_sunrise)


time_now = datetime.now()
