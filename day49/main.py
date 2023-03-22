"""
HACK: GoogleのOAuthでログインした。
    そして、OAuthの認証をブラウザ操作で行うのが難しい。（Googleの認証ボタンの取得がムズイ(一回、一回要素が変化する or クラス名が変わる（ex)buttonタグ、iframeタグ..etc）)。）
    なんでどうするか考える
    
    NOTE: もしかしたら、ホテルで貧弱なWi-Fiなのも、関係してたり？？？
    
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

time.sleep(10)

google_auth = driver.find_element(By.ID, 'sign-in-with-google-button')
google_auth.click()

time.sleep(10)


google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
email = driver.find_element(By.ID, 'identifierId')
email.send_keys(MY_EMAIL, Keys.ENTER)

time.sleep(4)

password = driver.find_element(By.NAME, 'password')
password.send_keys(MY_PASSWD, Keys.ENTER)

linkedin_window = driver.window_handles[0]
driver.switch_to.window(linkedin_window)

time.sleep(5)

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