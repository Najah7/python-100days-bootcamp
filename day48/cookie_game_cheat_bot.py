import os

# for dev
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import dotenv
dotenv.load_dotenv()
MS_DRIVER_PATH = os.getenv('MS_DRIVER_PATH')

Service = Service(executable_path=MS_DRIVER_PATH)
driver = webdriver.Edge(service=Service)

driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(4)
driver.find_element(By.ID, 'langSelect-JA').click()
time.sleep(4)
while True:
    time.sleep(2)
    driver.find_element(By.ID, 'bigCookie').click()