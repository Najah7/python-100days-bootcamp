import os
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import dotenv
dotenv.load_dotenv()
MS_DRIVER_PATH = os.getenv('MS_DRIVER_PATH')

TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')

PROMISED_DOWN = 100
PROMISED_UP = 10

GET_SPEED_URL = 'https://www.speedtest.net/'


# HACK&NOTE: 自分のアカウントの場合だけ使えるようになっているので、インターフェースを拡張するのもありかも

class TwitterBot:
    """Twitterにログインして、プロバイダへの文言をツイートする"""
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        service = Service(executable_path=MS_DRIVER_PATH)
        self.driver = webdriver.Edge(service=service)

    def _login_to_twitter(self):
        """Twitterにログインする関数（UI操作経由）"""
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        user_name_input = self.driver.find_element(By.CSS_SELECTOR, 'input' )
        user_name_input.send_keys(self.username, Keys.ENTER)
        time.sleep(2)
        password_input = self.driver.find_element(By.NAME, 'password' )
        password_input.send_keys(self.password, Keys.ENTER)
        time.sleep(5)

    


class InternetSpeedTwitterBot(TwitterBot):
    """インターネットの速度をチェックして、速度が遅い場合はプロバイダに文句をつぶやくボットクラス

        useage example:
        
            bot = InternetSpeedTwitterBot()
            bot.check_internet_and_tweet()
    
    
    """
    
    def __init__(self):
        super().__init__(TWITTER_USERNAME, TWITTER_PASSWORD)
        
        # NOTE:この処理に60秒かかってます。👇
        # なぜなら、利用しているサイトの仕様的に、最低でも40秒ほど待たなければならなく、余裕をもっての60秒にしています。
        # サイトのURL：https://www.speedtest.net/
        self._fetch_internet_speed()
        
        self.download_speed = self._get_dwonload_speed()
        self.upload_speed = self._get_upload_speed()
    
    
    # HACK:名前
    def check_internet_and_tweet(self):
        """インターネットの速度をチェックして、速度が遅い場合はプロバイダに文句をつぶやく関数"""
        if self.download_speed < PROMISED_DOWN or self.upload_speed < PROMISED_UP:
            self._tweet_at_provider()
        
    
    def _tweet_at_provider(self):
        """プロバイダへの文句をツイートする関数"""
        self._login_to_twitter()
        self.driver.get('https://twitter.com/compose/tweet')
        time.sleep(5)
        tweet_text = self.driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
        tweet_text.send_keys(self._generate_message(), Keys.CONTROL, Keys.ENTER)
        time.sleep(2)
        self.driver.quit()
        
    
        
    def _fetch_internet_speed(self):
        """インターネットの速度を取得する関数"""
        self.driver.get(GET_SPEED_URL)
        time.sleep(2)
        start_btn = self.driver.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a')
        start_btn.click()
        time.sleep(60)
        
        self._download_speed = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
        self._upload_speed =  float(self.driver.find_element(By.CLASS_NAME, 'upload-speed').text)
    
    def _generate_message(self):
        """ツイートするメッセージを生成する関数"""
        return f"pythonの練習でのツイートです（笑）。Hey Internet Provider, why is my internet speed {self.download_speed}down/{self.upload_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"  
        
    def _get_dwonload_speed(self):
        """インターネットのダウンロード速度を取得する関数"""
        return self._download_speed
    
    def _get_upload_speed(self):
        """インターネットのアップロード速度を取得する関数"""
        return self._upload_speed

