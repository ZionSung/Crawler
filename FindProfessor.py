from bs4 import BeautifulSoup
import requests
import os

res = requests.get("https://cs.ntcu.edu.tw/introduce/member#teachers")
print(res.text)