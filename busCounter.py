from bs4 import BeautifulSoup
import requests
import os

totalFirst = 0
totalSecond = 0

# ex 18~24 -> 18~25(24+1)
for date in range(18,25): 


    bus = "323" # change bus number
    inputDate = '2021-01-' + str(date)
    res = requests.get(f"http://citybus.taichung.gov.tw/cms/api/route/{bus}/timetable?date={inputDate}")
    #"http://citybus.taichung.gov.tw/cms/api/route/324/timetable?date=2021-01-18"
    soup = BeautifulSoup( res.text, 'lxml')
    text = soup.text

    print("=========")

    first = "1,"
    print(text.count(first))

    totalFirst = text.count(first) + totalFirst

    second = "2,"
    print(text.count(second))

    totalSecond = text.count(second) + totalSecond

print( "first = ", totalFirst )
print( "second = ", totalSecond )
