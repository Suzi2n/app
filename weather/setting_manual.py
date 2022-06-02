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
   # print(weather.text) # 날씨 웹크롤링


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





# music_list_ballad={'맑음':['김세정-SKYLINE','다비치-너에게 못했던 내 마지막 말은','백예린-Square','슬리피-기분탓'],
#                     '흐림':['태연-그대라는 시','악동뮤지션-어떻게 이별까지 사랑하겠어, 널 사랑하는거지','아이유-Love Poem','마크툽-마음이 말하는 행복'],
#                     '비':['규현-광화문에서','태연-U R','백예린-0310','PL-Umbrella'],
#                     '눈':['송이한-밝게 빛나는 별이 되어 비춰줄게','마크툽-별을 담은 시','에이치코드-꿈속에 너 (feat.전상근)','윤하-기다리다']
#                     } #딕셔너리 (발라드) 맑음,흐림,비,눈

# music_list_idol_m={'맑음':['투모로우바이투게더-어느날 머리에서 뿔이 자랐다','온앤오프-Complete','NCT DREAM-My page','슈퍼주니어-Devil'],
#                     '흐림':['세븐틴-Simple','비투비-아름답고도 아프구나','투모로바이투게더-drama','방탄소년단-Magic shop'],
#                     '비':['슈퍼주니어-비처럼 가지 마요','EXO-피터팬','비투비-그리워하다','SF9-돌고 돌아'],
#                     '눈':['비투비-울면 안 돼','방탄소년단-전하지 못한 진심','워너원-봄바람',' EXO-첫 눈']
#                     } #딕셔너리 (아이돌_남자) 맑음,흐림,비,눈


# music_list_idol_w={'맑음':['아이즈원-하늘 위로',' 태연- I',' 최예나- SMILEY','오마이걸- 한 발짝 두 발짝','우주소녀- UNNATURAL'],
#                     '흐림':['태연-INVU','여자아이들- 한',' 에이핑크- 덤더럼','마마무- wind flower'],
#                     '비':['아이오아이(I.O.I)-소나기','러블리즈- 그 시절 우리가 사랑했던 우리',' 에이핑크- 네가 손짓해주면','씨스타- LONELY'],
#                     '눈':['태연-만약에','러블리즈- 그날의 너',' 블랙핑크- STAY','아이즈원- 언젠가 우리의 밤도 지나가겠죠']
#                     } #딕셔너리 (아이돌_여자) 맑음,흐림,비,눈

# music_list_ost_korea={'맑음':['레드벨벳-Future','치즈-이렇게 좋아해 본 적이 없어요','양요섭,정은지-LOVE DAY','태일-Starlight'],
#                     '흐림':['김필- 어느 날 우리','케이윌- 내 생에 아름다운','산들- 취기를 빌려','Christopher- Moments'],
#                     '비':['폴킴- 모든날,모든순간','휘인- 너,너','거미- You are my everything','정승환-너였다면'],
#                     '눈':['백현- 나의 시간은','조정석- 아로하','헨리- It’s You','백예린- 다시 난, 여기','']
#                     } #딕셔너리 (ost_국내) 맑음,흐림,비,눈


# music_list_ost_other={'맑음':['Keala Settle – This is me','Glee Cast – Loser like me','Auli’i Cravalho - How Far I’ll Go (모아나 ost)','Shakira - Try Everything (주토피아 ost)'],
#                     '흐림':['Christina Perri-a thousand years','Adam Levine-Lost stars',' Ellie Goulding-Love me like you do','Loren Allred-Never Enough'],
#                     '비':['Celine Dion- My heart will go on','Zac Efon, Zendaya- Rewrite the stars','Naomi Scott – Speechless','Ed Sheeran – Photogragh'],
#                     '눈':['Idina Menzel – Show yourself','Ed Sheeran – Photogragh','Celine Dion- My heart will go on','Zac Efon, Zendaya- Rewrite the stars','']
#                     } #딕셔너리 (ost_국외) 맑음,흐림,비,눈


# music_list_jpop={'맑음':['오피셜히게단디즘 – universe','쿠보타 토시노부 – la la la love song','ZUTOMAYO – kan saete kuyashiiwa','호시노 겐 – koi'],
#                     '흐림':['whaledontsleep – 잠이 드는 거리','yonezu kenshi – 감전','tofubeats – 수성 (young&fresh remix)','吐息 - 紅い呪い'],
#                     '비':['ZUTOMAYO – obenkyou shitoiteyo','yama – 마비','yonezi kenshi – 춘뢰','spyair – winding road'],
#                     '눈':['오피셜히게단디즘 – pretender','세카이노오와리 – 환상의 생명','스다마사키, 요네즈 켄시 – 잿빛과 푸름','back number – 수평선']
#                     } #딕셔너리 (jpop) 맑음,흐림,비,눈

# music_list_dance={'맑음':['트리플 h – show me','보아 – 아틀란티스 소녀','프로미스9 - we go','브레이브 걸스 – 치맛바람'],
#                     '흐림':['범키 – 갖고놀래','보아 – one shot, two shot','태민 – drip drop','송지은 – 예쁜 나이 25살 '],
#                     '비':['태민 – goodbye','백예린 – antifreeze','샤이니 – 투명우산','애프터스쿨 – shampoo'],
#                     '눈':['exo – the star','브아걸, sg워너비 – must have love','오캬,뉴이스트 – 흰 눈 사이로 하이힐 타고','아이유 – 미리 메리크리스마스']
#                     } #딕셔너리 (댄스) 맑음,흐림,비,눈
# music_list_classic={'맑음':['카미유 생상스 – 동물의 사육제 : 백조','차이콥스키 – pas de deux','쇼팽 – 강아지 왈츠','슈베르트 – 아베 마리아'],
#                     '흐림':['쇼팽 – 녹턴 15번','쇼팽 – 발라드 1번 g단조 op.23','모차르트 – 론도 가단조'],
#                     '비':['최성훈 – io ti penso amore','안드레아 보첼리 – mi manchi','라포엠 – 초우'],
#                     '눈':['포르테디콰트로 – il libro dell’amore','드뷔시 – 달빛','satie – 짐 노페디 1번','슈만 – 트로이 메라이 어린이 정경 중 7번']
#                     } #딕셔너리 (클래식) 맑음,흐림,비,눈



# music_list_pop={'맑음':['Ed Sheeran-What Do I Know?','Anne-Marie-2002','Hamzaa-Sunday morning','uwu-Chevy'],
#                     '흐림':['Lauv-Paris In The Rain','GAYLE-abcdefu','HONNE-Day1','Daniel Caesar-Blessed'],
#                     '비':['Lauv-Paris In The Rain','Imagine Dragons-Thunder','Bruno Mars-It Will Rain','keshi-drunk'],
#                     '눈':['Kina Grannis-Creep','Mariah Carey-All I Want for Christmas Is You','Tori Kelly-25th','Tori kelly-Beautiful things','Adam Levine-Lost Stars']
#                     } #딕셔너리 (pop) 맑음,흐림,비,눈


# music_list_rockmetal_korea={'맑음':['노브레인-넌 내게 반했어','엔플라잉-봄이 부시게','언니네 이발관-산들산들','브로큰 발렌타인-Smashing your face','루시-개화'],
#                             '흐림':['델리스파이스-차우차우','짙은-백야','브로큰 발렌타인-알루미늄','검정치마-Everything'],
#                             '비':['델리스파이스-차우차우','잔나비-그대 떠나는 날 비가 오는가','짙은-백야','노브레인-비와 당신'],
#                     '눈':['정준일-새겨울','혁오-TOMBOY','잔나비-꿈과 책과 힘과 벽','넬-기억을 걷는 시간'],
#                     } #딕셔너리 (록/메탈_국내) 맑음,흐림,비,눈


# music_list_rockmetal_other={'맑음':['twenty one pilots-Morph','fun-Be Calm','Panic! At The Disco-C’mon','Maroon 5-One More Night','Amazing Blondel-A Spring Air'],
#                     '흐림':['Cage The Elephant-Cold Cold Cold','X Ambassadors-Renegades','Green Day-Wake Me Up When September Ends','Green Day-21guns','Nirvana-Smells Like Teen Spirit'],
#                     '비':[' Cage The Elephant-Cold Cold Cold','Imagine Dragons-Thunder','Imagine Dragons-Bad Day',' Plain White T’s-Hey There Delilah'],
#                     '눈':[' Cage The Elephant-Cold Cold Cold','Daniel Powter-Bad Day','fun-Some Nights',' Adam Levine-Lost Stars']
#                     } #딕셔너리 (록/메탈_국외) 맑음,흐림,비,눈



# music_list_fbc={'맑음':['Caamp-Believe','Home Free-Sea Shanty Medley',' Amazing Blondel-A Spring Air','The Minnesota Twins-Hey'],
#                     '흐림':[' Ziggy Alberts-TATTOOS','Woody Guthrie-This Land Is Your Land',' Peter, Paul & Mary-Puff, The Magic Dragon','Childsh Gambino, Brittany Howard-Stay High'],
#                     '비':['Caamp-Apple Tree Blues','James Taylor-Fire And Rain','Woody Guthrie-This Land Is Your Land','Townes Van Zandt-Pancho and Lefty'],
#                     '눈':['sewoong-before the lights come on','Priscilla Ahn-Dream','Mount Eerie-Real Death','Eric Clapton-White Christmas']
#                     } #딕셔너리 (포크/블루스/컨트리) 맑음,흐림,비,눈




# music_list_indie={'맑음':['백예린(Baek Yerin) - Square','STANDING EGG – 뭘까 ','DAY6(데이식스)-Emergency','윤하 – 오르트구름'],
#                     '흐림':['치즈(CHEEZE) - Romance','쏜애플(THORNAPPLE) - 시퍼런 봄',
#                     'Urban Zakapa(어반자카파) _ Thursday Night(목요일 밤)','비비(BIBI) - 사장님 도박은 재미로 하셔야 합니다(KAZINO)'],
#                     '비':['OOHYO(우효) _ PIZZA','심규선 - 폭풍의 언덕','알레프 (ALEPH) - Moodswing'],
#                     '눈':['전기뱀장어 (THE ELECTRICEELS) _ Yacht ','스텔라장 (Stella Jang) - 아무도 모르는 엔딩','jade - christmas at home','네이비쿼카 (NavyQuokka) - 그런 사람']
#                     } #딕셔너리 (인디) 맑음,흐림,비,눈



# music_list_newage={'맑음':['Duggy - cool summer!','Yutaka Hirasaka – Letter','Lucy – Outro'],
#                     '흐림':['Ryuichi Sakamoto – Opus','Norihiro Tsuru - Last Carnival','악토버(OCTOBER) - Acacia'],
#                     '비':['Ryuichi Sakamoto - A Flower Is Not a Flower','dvdkm – lonely','Evelyn Stein - Quiet Resource'],
#                     '눈':['Sakamoto Ryuichi - Merry Christmas Mr. Lawrence','이루마(Yiruma) - Indigo','레브(Reve) - Snowdrop']
#                     } #딕셔너리 (뉴에이지) 맑음,흐림,비,눈

# music_list_jazz={'맑음':['Nat King Cole – L-O-V-E','Red or White? - ABI','고상지 - 마지막 만담'],
#                     '흐림':['3월의 밤 (La Noche Del Marzo) - Dear Jazz Orchestra','LeonardCohen - Dance me to the end of love ','Iwamizu - 俗世／Zokuse'],
#                     '비':['Chet Baker - I get along without you very well ','Frank Sinatra – Fly Me to the Moon','Louis Armstrong - La Vie En Rose'],
#                     '눈':['Kurt Elling Leaving again  l  in the wee small hours','Doris Day - Put ''Em In A Box, Tie ''Em With A Ribbon (And Throw ''Em In The Deep Blue Sea)',
#                     'That Ole Devil Called Love - Billie Holiday']
#                     } #딕셔너리 (재즈) 맑음,흐림,비,눈








# genre_list=["발라드","아이돌_남자","아이돌_여자","ost_국내","ost_국외","jpop","댄스","클래식","POP","록/메탈_국내",
#             "록/메탈_국외","포크/블루스/컨트리","인디","뉴에이지","재즈"]

# print("")

# genre_select=input("취향 설정(하나 입력): ")     # 취향 설정 웹페이지로 입력 구현하기. 지금은 임시로 input으로 구현(genre_list에서 하나 입력)
# weather=i

# if genre_select in genre_list:
#     print(genre_select)
#     if genre_select == "발라드":
#             for key in music_list_ballad:
#                 print(', '.join(music_list_ballad[weather]))
#                 if weather == "맑음":
#                    webbrowser.open_new_tab('https://wmprogram.netlify.app/output_music.html')
#                    break
                
#                 if weather == "흐림":
#                    webbrowser.open_new_tab('https://wmprogram.netlify.app/output_music.html')
#                    break

#     if genre_select == "아이돌_남자":
#             for key in music_list_idol_m:
#                 print(', '.join(music_list_idol_m[weather]))
#                 if weather == "맑음":
#                     webbrowser.open_new_tab('listsite_idol_m1.html')
#                 break

#     if genre_select == "아이돌_여자":
#             for key in music_list_idol_w:
#                 print(', '.join(music_list_idol_w[weather]))
#                 break
#     if genre_select == "ost_국내":
#             for key in music_list_ost_korea:
#                 print(', '.join(music_list_ost_korea[weather]))
#                 break
#     if genre_select == "ost_국외":
#             for key in music_list_ost_other:
#                 print(', '.join(music_list_ost_other[weather]))
#                 break
#     if genre_select == "jpop":
#             for key in music_list_jpop:
#                 print(', '.join(music_list_jpop[weather]))
#                 break

#     if genre_select == "댄스":
#             for key in music_list_dance:
#                 print(', '.join(music_list_dance[weather]))
#                 break

#     if genre_select == "클래식":
#             for key in music_list_classic:
#                 print(', '.join(music_list_classic[weather]))
#                 break

#     if genre_select == "POP":
#             for key in music_list_pop:
#                 print(', '.join(music_list_pop[weather]))
#                 break

#     if genre_select == "록/메탈_국내":
#             for key in music_list_rockmetal_korea:
#                 print(', '.join(music_list_rockmetal_korea[weather]))
#                 break

#     if genre_select == "록/메탈_국외":
#             for key in music_list_rockmetal_other:
#                 print(', '.join(music_list_rockmetal_other[weather]))
#                 break

#     if genre_select == "포크/블루스/컨트리":
#             for key in music_list_fbc:
#                 print(', '.join(music_list_fbc[weather]))
#                 break

#     if genre_select == "인디":
#             for key in music_list_indie:
#                 print(', '.join(music_list_indie[weather]))
#                 break

#     if genre_select == "뉴에이지":
#             for key in music_list_newage:
#                 print(', '.join(music_list_newage[weather]))
#                 break

#     if genre_select == "재즈":
#             for key in music_list_jazz:
#                 print(', '.join(music_list_jazz[weather]))
#                 break

# else:
#     print("다시 입력하세요.")


