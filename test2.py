import requests
from bs4 import BeautifulSoup

location = input("지역을 입력하세요\n>>> ") 
Finallocation = location + '날씨' 
LocationInfo = "" 
NowTemp = "" 
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + Finallocation 
hdr = {'User-Agent': ('mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')} 
req = requests.get(url, headers=hdr) 
html = req.text 
soup = BeautifulSoup(html, 'html.parser') 
# 오류 체크 
ErrorCheck = soup.find('span', {'class' : 'btn_select'}) 

if 'None' in str(Finallocation): 
    print("Error! 지역 검색 오류!") 
else: 
    # 지역 정보 
    for i in soup.select('span[class=btn_select]'): 
        LocationInfo = i.text 
    
    NowTemp = soup.find(class_='temperature_text').text
       
    WeatherCast = soup.find(class_="weather before_slash").text 
    print("현재 온도 : " + NowTemp)
    print("현재 상태 : " + WeatherCast)
    


