from calendar import month
import requests
from bs4 import BeautifulSoup
from datetime import datetime

import webbrowser

from urllib.request import urlopen


location = input("지역을 입력하세요\n>>> ")
a = []
Finallocation = location + '날씨' 
LocationInfo = "" 
NowTemp = "" 
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + Finallocation 
hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
req = requests.get(url, headers=hdr) 
html = req.text 
soup = BeautifulSoup(html, 'html.parser') 
Month = datetime.today().month
Month = str(Month)
# 오류 체크 
ErrorCheck = soup.find('span', {'class' : 'btn_select'})
if 'None' in str(Finallocation): 
    print(text = "Error! 지역 검색 오류!") 
else: 
    # 지역 정보 
    for i in soup.select('span[class=btn_select]'): 
        LocationInfo = i.text     
    NowTemp = soup.find(class_='temperature_text')
    temp = NowTemp.text
    temp = float(temp.strip(' 현재온도°'))
    temp = int(temp)
    weather= soup.find(class_='weather before_slash')


    print(temp)
   print(weather.text) # 날씨 웹크롤링


if '1' in str(Month) or '2' in str(Month) or '11' in str(Month) or '12' in str(Month):
    a.append('눈')
    for i in a:
        print(i, " ", end='') # a.append에 적힌 날씨 출력
    
elif '눈' in str(weather):
    a.append('눈')
    for i in a:
        print(i, " ", end='')

elif '비' in str(weather):
    a.append('비')    
    for i in a:
        print(i, " ", end='')

elif '흐림' in str(weather):
    a.append('흐림')
    for i in a:
        print(i, " ", end='')

elif '맑음' in str(weather):
    a.append('맑음')
    for i in a:
        print(i, " ", end='')

elif '구름많음' in str(weather):
    a.append('흐림')
    for i in a:
        print(i, " ", end='')
elif '번개' in str(weather):
    a.append('비')
    for i in a:
        print(i, " ", end='')

elif '구름조금' in str(weather):
    a.append('맑음')
    for i in a:
        print(i, " ", end='')


weather=i

if weather == "맑음":
    webbrowser.open_new_tab('https://wmprogram.netlify.app/taste_settings_sunny.html')

if weather == "흐림":
    webbrowser.open_new_tab('https://wmprogram.netlify.app/taste_settings_blur.html')

if weather == "비":
    webbrowser.open_new_tab('https://wmprogram.netlify.app/taste_settings_rainy.html')

if weather == "눈":
    webbrowser.open_new_tab('https://wmprogram.netlify.app/taste_settings_snow.html')
