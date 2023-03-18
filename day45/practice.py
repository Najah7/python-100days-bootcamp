from bs4 import BeautifulSoup

# NOTE:ためにlxmlフォーマットのサイトもあるから、その時は下記のモジュールのパーサを使う👇
# import lxml

with open('website.html', 'r') as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title) # title要素
print(soup.title.name) # タグ名
print(soup.title.string) # コンテンツの文字

# NOTE：きれいにフォーマットしてくれている👇
print(soup)

all_a_tags = soup.find_all(name='a')
print(all_a_tags)

for a_tag in all_a_tags:
    print(a_tag.getText())
    print(a_tag.get('href'))
    
haeding = soup.find(name='h1', id='name')
print(haeding)

section_heading = soup.find(name='h3', class_='heading')
print(section_heading)

# NOTE:CSSのセレクタと使い方おなじ👇
heading = soup.select(".heading")
print(heading)

company_url = soup.select_one(selector='p a')
print(company_url)