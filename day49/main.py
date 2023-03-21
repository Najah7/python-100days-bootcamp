"""
HACK: GoogleのOAuthでログインした。
    そして、OAuthの認証をブラウザ操作で行うのが難しい。（Googleの認証ボタンの取得がムズイ。）
    なんでどうするか考える
    
NOTE:解決策NOTE
    ・シンプルにベーシック認証でアカウントを作る。
    
"""

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

MY_EMAIL = os.getenv('MY_EMAIL')
MY_PASSWD = os.getenv('My_PASSWD')

Service = Service(executable_path=MS_DRIVER_PATH)
driver = webdriver.Edge(service=Service)

driver.get('https://www.linkedin.com/login/en')

# time.sleep(3)

# email = driver.find_element(By.ID, 'username')
# email.send_keys(MY_EMAIL)


time.sleep(3)

# google_button = driver.find_element(By.XPATH, '//*[@id="container"]/div')

# google_button = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div'))
# )
# print('test:', google_button)
# google_button.click()

# auth_btn = driver.find_element(By.CSS_SELECTOR, '#gsi_219294_448508')
# auth_btn.click()

# time.sleep(10)

driver.quit()