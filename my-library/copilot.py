# Webサイトのスクレイピングを行う
# 1. ライブラリのインポート

import requests
from bs4 import BeautifulSoup

# 2. WebサイトのURLを指定

url = "https://www.ymori.com/books/python2nen/test2.html"

# 3. Webサイトからデータを取得

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# 4. データを解析

elems = soup.find_all("li")

# 5. データを保存

for e in elems:

    print(e.getText())

# 6. データを表示

for e in elems:

    print(e.getText())
