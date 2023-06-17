from bs4 import BeautifulSoup
import requests

# TIS.incのWebサイトからスクレイピングを使ってニュース一覧を取得し表示する。
url = 'https://www.tis.co.jp/news/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
news_list = soup.find_all('a', class_='infoList')
for news in news_list:
    print(news)
