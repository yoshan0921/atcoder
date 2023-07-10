# ニュース一覧HTMLの生成
#
# news.txtの内容を読み込んで、ニュース一覧のHTMLを生成してください。
# 生成するHTMLのファイル名はnews.htmlとしてください。
# txtファイルは以下の形式で保存されています。
# ・日付（改行）
# ・タイトル（改行）
# ・URL（改行）
# ニュース一覧はtable要素を使ってテーブル形式で出力してください。
# テーブルの罫線はグレー色にしてください。
# テーブルの各行には以下の内容を出力してください。
# ・日付
# ・タイトル（a要素でリンク形式にしてください。a要素のhref属性にはURLを指定してください。）

# ここにコードを書いてください。
import requests
from bs4 import BeautifulSoup

with open('news.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('news.html', 'w', encoding='utf-8') as f:
    f.write('<table border="1" style="border-color: gray;">\n')
    for i in range(0, len(lines), 3):
        f.write('<tr>\n')
        f.write('<td>{}</td>\n'.format(lines[i].rstrip()))
        f.write(
            '<td><a href="{}">{}</a></td>\n'.format(lines[i+2].rstrip(), lines[i+1].rstrip()))
        f.write('</tr>\n')
    f.write('</table>\n')
