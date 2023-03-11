import os
import smtplib

# load Environment variables
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv('PASSWORD')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    def send_email(self, message):
        with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Low price alert!🛫\n\n{message}"
            )