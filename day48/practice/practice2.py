"""
Practice with Selenium
"""
import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import dotenv
dotenv.load_dotenv()
MS_DRIVER_PATH = os.getenv('MS_DRIVER_PATH')


service = Service(executable_path=MS_DRIVER_PATH)
driver = webdriver.Edge(service=service)


# Open a web page
driver.get('https://python.org/')

# get the search box
event_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, '.event-widget a')[1:]

event_times = [event_time.text for event_time in event_times if event_time.text != '']
event_names = [event_name.text for event_name in event_names if event_name.text != '']



if len(event_times) == len(event_names):
    with open('python-events.csv', 'w') as csv_file:
        csv_file.write('date, event name')
        for i in range(len(event_times)):
            csv_file.write(f"{event_times[i].strip(' ')}, {event_names[i].strip(' ')}\n")

