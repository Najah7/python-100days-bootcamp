# HACK:外部に公開しないやつ（「_」で始まるやつはもう一段階抽象化してもいいかも...）

# NOTE:datetime.datetime().strtime():https://www.w3schools.com/python/python_datetime.asp


import datetime as dt
import requests
import os

from dotenv import load_dotenv
load_dotenv()

# NOTE:tokenを作るときに便利👇
"""
import secrets
print(secrets.token_hex())
"""

TOKEN = os.getenv('TOKEN')

USERNAME = 'najah'

PIXELA_USER_ENDPONT = 'https://pixe.la/v1/users'
PIXELA_GRAPH_ENDPONT = f'{PIXELA_USER_ENDPONT}/{USERNAME}/graphs'


def _params_to_create_user():
    
    params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
    }
    
    return params
def _params_to_create_graph(id, graph_name, unit, type, color):
    
    params = {
        'id': id,
        'name': graph_name,
        'unit': unit,
        'type': type,
        'color': color,
    }
    
    return params


def _params_to_create_pixel(quantity, date=None):
    
    if date is None:
        now = dt.datetime.now()
        date = now.strftime("%Y%m%d")
        
    
    params = {
        'date': date,
        'quantity': quantity,
    }
    
    return params

def _params_to_update_pixel(quantity):
    params = {
        'quantity': quantity
    }
    
    return params
    
def _header_with_token():
    
    header = {
        'X-USER-TOKEN': TOKEN
    }
    
    return header
    

def create_user():
    """最初にユーザを作成するためのリクエストを実行する関数。
        レスポンスを返す。
        NOTE:※一度だけ実行する関数なので、「_」で始めた
    """
    
    params = _params_to_create_user()
    res = requests.post(PIXELA_USER_ENDPONT, json=params)
    
    return res

def create_graph(id, graph_name, unit, type, color):
    """グラフを作成して、responseを返す関数"""
    
    params = _params_to_create_graph(id, graph_name, unit, type, color)
    res = requests.post(url=PIXELA_GRAPH_ENDPONT, json=params, headers=_header_with_token())
    
    return res

def create_pixel(graph_id, quantity, date=None):
    
    endpoint_to_post = f'{PIXELA_GRAPH_ENDPONT}/{graph_id}'
    params = _params_to_create_pixel(quantity, date)
    
    res = requests.post(endpoint_to_post, json=params, headers=_header_with_token())
    
    return res

def update_pixel(graph_id, quantity, date=None):
    
    if date is None:
        now = dt.datetime.now()
        date = now.strftime('%Y%m%d')
    
    endpont = f"{PIXELA_GRAPH_ENDPONT}/{graph_id}/{date}"
    params = _params_to_update_pixel(quantity)
    
    res = requests.put(endpont, json=params, headers=_header_with_token())
    
    return res

def delete_pixel(graph_id, date=None):
    
    if date is None:
        now = dt.datetime.now()
        date = now.strftime('%Y%m%d')
        
    endpoint = f"{PIXELA_GRAPH_ENDPONT}/{graph_id}/{date}"
    
    res = requests.delete(endpoint, headers=_header_with_token())
    
    return res