##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
import os

from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')

df_birthdays = pandas.read_csv('birthdays.csv')

now = dt.datetime.now()
today_tuple = (now.month(), now.day())

birthdays_dict = { (data_row.month, data_row.day): data_row for (index, data_row) in df_birthdays.iterrows() }

if today_tuple in birthdays_dict:
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    birthday_person = birthdays_dict[today_tuple]
    
    with open(file_path, 'r') as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])
    
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )      
    



