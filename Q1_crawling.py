import requests
import bs4
from bs4 import BeautifulSoup as bs

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'}

data = requests.get(url, headers=headers)

soup = bs(data.text, 'html.parser')
td = soup.select("#old_content > table > tbody > tr")

for i in td:
    movie = []
    td_num = i.select_one('.ac > img')
    td_title = i.select_one('div > a')
    td_point = i.select_one('.point')
    if td_title is not None:
        movie.append(td_num['alt'] + " " +td_title.text + " " + td_point.text)
        movie = movie[0]
        print(movie)