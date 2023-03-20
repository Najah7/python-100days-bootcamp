import os
import smtplib
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
HACK: fetchしすぎて、セキュリティではじかれたので、in progressです。
    少し時間をおいて、再度確認します。
    
    詳細：一応、本のタイトル取得まではＯＫっぽい（まだ今日のバージョンしか確認できてないけど）
        Emailのところを実装中にはじかれたので、そっちは未確認です。
"""


# NOTE:完全な個人的な趣向でMSを使っています😅
# 　　　多分、Chromeとかの方が情報あって使いやすいかも。。。

import dotenv
dotenv.load_dotenv()

MS_DRIVER_PATH = os.getenv('MS_DRIVER_PATH')

MY_EMAIL = os.getenv('MY_EMAIL')
EMAIL_PASSWORD = os.getenv('PASSWORD')

def main():

    service = Service(executable_path=MS_DRIVER_PATH)
    driver = webdriver.Edge(service=service)

    # driver.get('https://www.bing.com/?setlang=ja-JP')

    # search_box = driver.find_element(By.NAME, 'q')
    # print(search_box.get_attribute('placeholder'))
    # search_box.send_keys('kindle 日替わりセール', Keys.ENTER)
    # elems = driver.find_elements(By.XPATH, '//*[@id="b_results"]/li[2]/div[1]/h2/a')

    # NOTE:MSではうまくいかなかったので、Googleで検索

    driver.get('https://www.google.com/')

    # get the search box
    search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')
    # search for 'kindle 日替わりセール'
    search_box.send_keys('kindle 日替わりセール', Keys.ENTER)

    # find the link and go to the page
    elems = driver.find_elements(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div[2]/ul/li/div/div/div/div[1]/div/a')
    for elem in elems:
        url = elem.get_attribute('href')
        if '/kindle-dbs/' in url:
            driver.get(url)
            break

    # get the book titles
    book1 = driver.find_element(By.XPATH, '//*[@id="browse-grid-view"]/div[1]/a/div/div[2]/ul/li[1]/span/span')
    book2 = driver.find_element(By.XPATH, '//*[@id="browse-grid-view"]/div[2]/a/div/div[2]/ul/li[1]/span/span')
    book3 = driver.find_element(By.XPATH, '//*[@id="browse-grid-view"]/div[3]/a/div/div[2]/ul/li[1]/span/span')

    # check the book titles (for dev)
    # print(book1.text)
    # print(book2.text)
    # print(book3.text)
    
    # for dev
    # time.sleep(1)
    
    driver.quit()
    
    send_email(book1.text, book2.text, book3.text)
    
    

    

def send_email(book1, book2, book3):
    """send email to myself"""
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Todays's Kindle discount books are:\n{book1}\n{book2}\n{book3}"
        )
    

if __name__ == '__main__':
    main()