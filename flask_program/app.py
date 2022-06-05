from flask import Flask, render_template ,request,url_for

from flask import Flask, render_template, url_for, request
from calendar import month
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json
import googlemaps

from pyowm import OWM
from pyowm.utils.config import get_default_config

import webbrowser
from urllib.request import urlopen

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/manual')
def manual():
    return render_template("manual.html")



@app.route("/result", methods = ['POST', "GET"])

@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    a = []
    Finallocation = name + '날씨' 
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
        print(weather.text)

    if '1' in Month or '2' in Month or '11' in Month or '12' in Month:
        a.append('눈')
        print(a)

    elif '눈' in str(weather):
        a.append('눈')
        print(a)
    elif '비' in str(weather):
        a.append('비')    
        print(a)
    elif '흐림' in str(weather):
        a.append('흐림')
        print(a)
    elif '맑음' in str(weather):
        a.append('맑음')
        print(a)
    elif '구름많음' in str(weather):
        a.append('흐림')
        print(a)
    elif '번개' in str(weather):
        a.append('비')
        print(a)
    elif '구름조금' in str(weather):
        a.append('맑음')
        print(a)


    return render_template('manual.html', name = name, a = a[0] )



@app.route('/auto')
def auto():
    #output = request.form.to_dict()
    #print(output)

    #name = output["name"]
    GOOGLE_API_KEY = 'AIzaSyCKqc__yNSlC-9IspRAZWxU7GskBv6-z-8'
    API_key = '27c674b1ce585ff4aea4fc73ac8b3d32'

    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}'
    data = {
        'considerIp': True, #현 IP로 데이터 추출
    }

    result = requests.post(url, data) # 해당 API에 요청을 보내며 데이터를 추출

    print(result.text)
    result2 = json.loads(result.text)

    lat = result2["location"]["lat"] # 현재 위치의 위도 추출
    lng = result2["location"]["lng"] # 현재 위치의 경도 추출



    config_dict = get_default_config()
    config_dict['language'] = 'kr' #언어 설정

    owm = OWM(API_key, config_dict)
    mgr = owm.weather_manager()
    obs = mgr.weather_at_coords(lat, lng)
    w = obs.weather

    print(w.detailed_status) #자동설정 구글날씨 크롤링

    a=[]


    if '맑음' in str(w.detailed_status):
        a.append('맑음')
        print(a)
            
    if '흐림' in str(w.detailed_status):
        a.append('흐림')
        print(a)
            

    if '비' in str(w.detailed_status):
        a.append('비')
        print(a)
            

    if '눈' in str(w.detailed_status):
        a.append('눈')
        print(a)
            

   # else:
   #     print("음악리스트를 찾을 수 없습니다.")



    return render_template("auto.html", a=a[0])



if __name__ == '__main__':
    app.run(debug=True) 