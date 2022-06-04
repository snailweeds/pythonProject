import requests
import bs4
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

matrix = db.movies.find_one({'title':'매트릭스'})
matrix_star = matrix['star']
print(matrix_star)
allmovies = db.movies.find({'star':matrix_star})
for samematrix in allmovies:
    samemovie = samematrix['title']
    print(samemovie)

db.movies.update_one({'title':'매트릭스'}, {'$set': {'star':'0'}})
print(matrix)