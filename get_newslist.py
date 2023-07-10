# ニュース一覧の取得（Webスクレイピング）
#
# ターゲットサイトはTIS.incのWebサイトです。
# URLはhttps://www.tis.co.jp/ir/news/です。
# classがinfoListのul要素の下にある各li要素から情報を取得してください。
# 取得する情報は以下の通りです。
# ・日付 time要素のdatetime属性
# ・タイトル a要素のテキスト
# ・URL a要素のhref属性
# URLが相対パスになっているものは、絶対パスに変換してください。
# 文字化けしないようにresponseオブジェクトのcontent属性を使ってください。
# 取得したデータはnews.txtというファイルに書き込んでください。
# 日付、タイトル、URLは改行区切りで書き込んでください。
# 文字コードはUTF8を指定してください。

# ここにコードを書いてください。
import requests
from bs4 import BeautifulSoup

url = 'https://www.tis.co.jp/ir/news/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

with open('news.txt', 'w', encoding='utf-8') as f:
    for li in soup.find('ul', class_='infoList').find_all('li'):
        date = li.find('time')['datetime']
        title = li.find('a').text
        url = li.find('a')['href']
        if url.startswith('/'):
            url = 'https://www.tis.co.jp' + url
        f.write(date + '\n')
        f.write(title + '\n')
        f.write(url + '\n')
