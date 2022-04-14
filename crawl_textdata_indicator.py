""" Created by MrBBS """
# 4/12/2022
# -*-encoding:utf-8-*-

import requests
from bs4 import BeautifulSoup

# query = input("What would you like to search: ")
query = 'sidewalk Gregariousness'
print('keywords: ', query)
query = query.replace(" ", "+")
query = "https://www.google.com/search?q=" + query

r = requests.get(query)
html_doc = r.text

soup = BeautifulSoup(html_doc, 'html.parser')
results = set()
for s in soup.find_all(class_="BNeawe s3v9rd AP7Wnd"):
    result = ''.join(s.text.split('·')[1:]).strip()
    if len(result) > 0:
        results.add(result)

print(results)
