"""
Project Amazon Price Tracker
"""

"""
NOTE:Amazonのスクレーピング対策がなかなかで、短時間で解決できそうにないので、諦め。
       シンプルにAPIの勉強として、AmazonのAPIを使ってなら、簡単に実装できそう。

ChatGPT NOTE:
    Amazonは、ウェブスクレイピングの対象として非常に複雑なサイトの1つです。これは、多数の動的な要素があるためです。たとえば、商品の価格や在庫状況、レビューなどは、常に変化する可能性があります。また、Amazonは、ウェブスクレイピングを防止するためのさまざまな技術を使用しているため、自動化されたスクレイピングをより困難にしています。
    そのため、Amazonをスクレイピングすることは、初心者にとってはかなり難しいかもしれません。ただし、高度なプログラミングスキルやウェブスクレイピングの経験を持っている場合は、Amazonをスクレイピングすることは可能です。ただし、Amazonの利用規約に違反することなくスクレイピングを行う必要があるため、注意が必要です。

"""



from bs4 import BeautifulSoup
import requests
import lxml
import os

from dotenv import load_dotenv
load_dotenv()

# NOTE:URLに埋め込む形のToken認証なので、URLを公開していいかわからなかったので、環境変数に
url = os.getenv('URL')

"""
HACK:URLにトークンを埋め込むタイプなので、スクレーピングは難しめ（多分JWTなのかな...）
    動画ではスクレーピングしてたけど、Amazon Product Advertising APIを使うのをおすすめ（bottlenose使って）
"""
headers = {
    'Accept-Language': 'ja,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'Uesr-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.content, "lxml")

print(soup.prettify())

price = soup.find(name='span', class_='a_price_whole')
print(price)