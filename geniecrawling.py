import requests
import bs4
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'}
url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1'
data = requests.get(url, headers = headers)
soup = bs(data.text, 'html.parser')
lists = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for i in lists:
    pnumber = i.select_one('.number').text.strip().replace("\n", "")
    child_num = i.select_one('.number > span').text.strip().replace("\n", "")
    number = pnumber.replace(child_num, "").strip()
    title = i.select_one('td.info > a').text.replace("\n", "").strip()
    artist = i.select_one('td.info > a.artist.ellipsis').text
    if number is not None:
        print(number, title, artist)