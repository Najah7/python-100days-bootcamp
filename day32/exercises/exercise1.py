"""
Project Send Quote Everyday.
"""

import smtplib
import random
import os


with open('quotes.txt', 'r') as file:
    quotes = [quote for quote in file.readlines()]

def today_quote():
    today_quote = random.choice(quotes)
    return today_quote

from dotenv import load_dotenv
load_dotenv()

my_email = os.getenv('MY_EMAIL')
password = os.getenv('PASSWORD')

message = f'Subject:Today Quote\n\n{today_quote()}'

# NOTE:withを使うことでcloseする必要がなし
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=message
    )