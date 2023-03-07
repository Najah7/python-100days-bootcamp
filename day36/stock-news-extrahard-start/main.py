"""
Project Stack
"""

import requests
import os
import datetime as dt
import smtplib
import unicodedata

# for dev 
from pprint import pprint


# ============================ Constants =============================
from dotenv import load_dotenv
load_dotenv()

# Stock API info
STOCK_API_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = os.getenv('STOCK_API_KEY')

# News API info
NEWS_API_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NUM_ARTICLES = 5

# Gmail Access info
MY_EMAIL = os.getenv('MY_EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

# TESLA info
STOCK_SYMBOL = "TSLA"
COMPANY_NAME = "Tesla Inc"

diff_percent = 0
up_down = ""

# ============================ Main Logic =============================
def main():
    
    # call Stock API
    # NOTE:refer to https://www.alphavantage.co/documentation/ to see API design
    stock_res_json = fetch_json_TSLA_dairy()
    
    # format fetched data
    dairy_time_series = format_stock_res(stock_res_json)
    
    # get closing prices
    yesterday_closing_price = get_yesterday_closing_price(dairy_time_series)
    day_before_yesterday_closing_price = get_day_before_yesterday_closing_price(dairy_time_series)
    
    # check if there was big change
    # 
    if was_big_change(
        yesterday_closing_price,
        day_before_yesterday_closing_price
        ):
        
        global up_down
        global diff_percent
        
        # call News API
        news_res_json = fetch_TSLA_news()
        articles = get_articles(news_res_json, num=NUM_ARTICLES)
        
        content = str()
        
        
        for article in articles:
            content += f'{STOCK_SYMBOL} : {up_down} {diff_percent}% '
            content += f"Headline: {article['title']}\n"
            content += f"Description: {article['description']}\n"
            content += "\n\n"
            
        content = unicodedata.normalize("NFKD", content)
        
        # send mail 
        send_email(content)
    
     
# ============================ Stock Helper Funcs =============================
def fetch_json_TSLA_dairy():
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': STOCK_SYMBOL,
        'apikey': STOCK_API_KEY
    }
    res = requests.get(STOCK_API_ENDPOINT, params=params)
    res.raise_for_status()
    return res.json()


def format_stock_res(res):
    dairy_time_series = res['Time Series (Daily)']
    dairy_time_series = [ value for key, value in dairy_time_series.items()]
    
    return dairy_time_series

def get_yesterday_closing_price(dairy_time_series):
    yesterday_info = dairy_time_series[0]
    closing_price = float(yesterday_info['4. close']) 
    
    return closing_price

def get_day_before_yesterday_closing_price(dairy_time_series):
    day_befor_yesterday_info = dairy_time_series[1]
    day_before_yesterday_closing_price = float(day_befor_yesterday_info['4. close'])
    
    return day_before_yesterday_closing_price

def was_big_change(yesterday_closing_price, day_before_yesterday_closing_price):
    
    diff = yesterday_closing_price - day_before_yesterday_closing_price
    
    global up_down
    if diff > 0:
        up_down = '🆙'
    else:
        up_down = '🔽'
    
    global diff_percent
    diff_percent = (abs(diff) / float(yesterday_closing_price)) * 100
    
    if diff_percent >= 5:
        return True
    return False

# ============================ NEWS Helper Funcs ===================
def fetch_TSLA_news():
    params= {
        'qInTitle': COMPANY_NAME,
        'apiKey': NEWS_API_KEY
    }
    
    res  = requests.get(NEWS_API_ENDPOINT, params=params)
    res.raise_for_status()
    return res.json()

def get_articles(res, num=5):
    return res['articles'][:num]
    
# ============================ Mail Helper Funcs ===================

def send_email(content):
    
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Shoud check news\n\n{content}"
        )


if __name__ == '__main__':
    main()
   
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# import requests

# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2023-03-08&'
#        'sortBy=popularity&'
#        'apiKey=ce758d594f5a4000a3e787f1ae25b65d')

# response = requests.get(url)

# print r.json


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


    