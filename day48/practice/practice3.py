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

# レスポンシブにより、要素が見えなくなるので、大きめにしています。（検索ボックスなど）
driver.set_window_size(1600, 1200)


driver.get('https://en.wikipedia.org/wiki/Main_Page')

num_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# num_articles.click()
num_articles = num_articles.text.replace(',', '')
num_articles = int(num_articles)

search_box = driver.find_element(By.NAME, 'search')
search_box.send_keys('Python', Keys.ENTER)


time.sleep(1)

driver.get()



print(num_articles)