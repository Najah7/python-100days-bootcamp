import os
import smtplib
import datetime as dt

# for using Gmail
from dotenv import load_dotenv
load_dotenv()

# my_email = os.getenv('MY_EMAIL')
# password = os.getenv('PASSWORD')

# # NOTE:withを使うことでcloseする必要がなし
# with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg='Subject:Hello\n\nThis is the body of my email'
#     )

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() #monday is 0
print(day_of_week)

date_of_birth = dt.datetime(year=2001, month=10, day=25)
print(date_of_birth)