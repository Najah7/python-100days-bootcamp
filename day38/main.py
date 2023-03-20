"""
Project Exercise Recorder on Google sheet
"""

# HACK:翻訳機能を入れて日本語対応させる。
# SOLVED:WLS2にはデフォルトで日本語フォントが入ってなかったので、インストールした。

import datetime as dt
import requests
import os

# for dev 
from pprint import pprint

# load Environment variables
from dotenv import load_dotenv
load_dotenv()


# nutritionix
# NOTE:refer to https://developer.nutritionix.com/
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")


# Sheety
# NOTE:refer to https://sheety.co/docs/requests
SHEET_ENDPONT = os.getenv('SHEET_ENDPOINT')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')


# constants 
GENDER = 'male'
WEIGHT_kg = 73
HEIGHT = 184
AGE = 21


def main():

    exercise_name = input("Tell me which exercies you did: ")
    
    exercise_res = fetch_exercise_info(exercise_name).json()
    
    sheet_res = record_exercise_on_spredsheet(exercise_res).json()
    
    pprint(sheet_res)

def headers_with_bearer_token():
    """Sheetyの認証に必要なheaderを返す関数"""
    
    headers = {
        'Authorization': SHEETY_TOKEN,
    }
    
    return headers
    
def fetch_exercise_info(exercise_name):
    """exerciseの名前をもとに、exerciseの情報をフェッチし、レスポンスを返す関数。"""
    
    headers = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY,
    }
    
    params = {
    'query': exercise_name,
    'gender': GENDER,
    'weight_kg': WEIGHT_kg,
    'height_cm': HEIGHT,
    'age': AGE
    }
    
    res = requests.post(EXERCISE_ENDPOINT, json=params, headers=headers)
    
    return res

def get_today():
    """今日の日付を返す関数"""
    return dt.datetime.now().strftime('%Y/%m/%d')

def get_time_now():
    """今の時間を返す関数"""
    return dt.datetime.now().strftime("%X")

def record_exercise_on_spredsheet(exercise_res):
    """APIをcallして、スプレットシートにデータを保存して、APIのレスポンスを返す関数"""
    
    headers = headers_with_bearer_token()
    
    today = get_today()
    time_now = get_time_now()
    
    for exercise in exercise_res['exercises']:
        params = {
            'workout': {
                'date': today,
                'time': time_now,
                'exercise': exercise['name'].title(),
                'duration': exercise['duration_min'],
                'calories' : exercise['nf_calories'],
            }
        }
    
    res = requests.post(SHEET_ENDPONT, json=params, headers=headers)
    
    return res
    
if __name__ == '__main__':
    main()