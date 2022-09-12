# Donwolad data 2

import requests as r
from bs4 import BeautifulSoup

URL = 'https://www.kantor.pl'
page = r.get(URL)

bs = BeautifulSoup(page.content, 'html.parser')
#print(page.status_code)

for informations in bs.find_all('div', class_='currency-block'):
    names = informations.find('span', class_='curr-label')
    operation = informations.find_all('div', class_='curr-operation-rate')
    
    print(names.text, 'kupno: ', operation[0].text,' sprzedaż: ', operation[1].text)
