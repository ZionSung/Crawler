from bs4 import BeautifulSoup
import requests
import os

res = requests.get("https://cs.ntcu.edu.tw/introduce/member#teachers")
soup = BeautifulSoup( res.text, 'lxml')

#professors = soup.select('div.col-12')
for professor in soup.select('#teachers .col-12'):
    name = professor.find('h5')
    print(name.text)
    for data in professor.find_all('li'):
        print(data.text)