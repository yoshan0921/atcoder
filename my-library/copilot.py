# ニュース一覧の取得
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
    for tag in soup.find('ul', class_='infoList').find_all('li'):
        date = tag.find('time').get('datetime')
        title = tag.find('a').get_text()
        href = tag.find('a').get('href')
        if href.startswith('/'):
            href = 'https://www.tis.co.jp' + href
        f.write(f'{date}\n{title}\n{href}\n\n')


# news.txtの内容を読み込んで、ニュース一覧のHTMLを生成してください。
# 生成したHTMLはnews.htmlというファイルに書き込んでください。
# タイトルにニュース
# 表示するする情報は以下の通りです。
# ・日付
# ・タイトル
# ・URL

# ここにコードを書いてください。
with open('news.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('news.html', 'w', encoding='utf-8') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<meta charset="utf-8">\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<ul>\n')
    for i in range(0, len(lines), 4):
        f.write(
            f'<li>{lines[i].strip()}<br>{lines[i+1].strip()}<br><a href="{lines[i+2].strip()}">{lines[i+2].strip()}</a></li>\n')
    f.write('</ul>\n')
    f.write('</body>\n')
    f.write('</html>\n')
