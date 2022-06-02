fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for fruit in fruits:
    print(fruit);

for person in people:
    if person['age'] < 20:
        print(person['name'])

# --------------------------------------------------------------------------

import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    gu_name = gu['MSRSTE_NM']
    if gu['IDEX_MVL'] < 60:
        print(gu_name)

# --------------------------------------------------------------------------

import bs4

from bs4 import BeautifulSoup as bs

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = bs(data.text, 'html.parser')

titles = soup.select('#old_content > table > tbody > tr')
for title in titles:
    title = title.select_one('td.title > div > a')
    if title is not None:
        print(title.text)