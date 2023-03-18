from bs4 import BeautifulSoup
import requests

TARGET_URL = 'https://news.ycombinator.com/'

res = requests.get(TARGET_URL)
web_page_html = res.text

soup = BeautifulSoup(web_page_html, 'html.parser')
article_tags = soup.find_all(name='a', class_='storylink')

article_texts = []
article_links = []

for tag in article_tags: 
    article_texts.append(tag.getText())
    article_links.append(tag.get('href'))
    
article_upvotes = [score.getText().split()[0] for score in soup.find_all(name='span', class_='score')]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts, article_links, article_upvotes)
