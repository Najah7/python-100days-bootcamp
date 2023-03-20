"""
Practice with Selenium
"""
import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# NOTE:完全な個人的な趣向でMSを使っています😅
# 　　　多分、Chromeとかの方が情報あって使いやすいかも。。。

import dotenv
dotenv.load_dotenv()
MS_DRIVER_PATH = os.getenv('MS_DRIVER_PATH')


service = Service(executable_path=MS_DRIVER_PATH)
driver = webdriver.Edge(service=service)

"""
Search for 'Selenuim' on Google
"""

"""
Selenium vs BeautifulSoup

Selenium:　ブラウザを操作するためのライブラリ（動的用（JSが関わる））
BeautifulSoup:　HTMLをパースするためのライブラリ（静的用）
"""

# Open a web page
driver.get('https://www.google.com/')

# get the search box
search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')
# search for 'Selenuim'
search_box.send_keys('Selenuim', Keys.ENTER)

"""
Search for requests module on PyPI
"""
driver.get('https://pypi.org/')
search_box = driver.find_element(By.ID, 'search')
search_box.send_keys('requests', Keys.ENTER)

"""
Other way to get elements
"""
driver.get('https://pypi.org/')
driver.find_element(By.CSS_SELECTOR, 'input#search')
# NOTE:XPathは、HTMLの構造を見て、要素を特定するための方法。
content = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/p/a')
print(content.text)


driver.close() # close current tab
driver.quit() # close all tabs