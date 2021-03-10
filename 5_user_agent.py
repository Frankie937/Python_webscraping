# 네이버에 접속할 때, 데스크탑으로 접속하면 넓은 화면으로 보이고 스마트폰으로 접속하면 모바일에 맞는 화면으로 보임
# 즉, 브라우저가 웹사이트에 접속할 때 주는 헤더 정보에 따라서 사이트가 줄 화면을 선택해서 줄 수 있음 
# 그런데 사람이 접속하는 것이 아니라, 웹 스크래핑이나 웹 크롤링하는 컴퓨터가 접속하여 무단으로 정보를 끌고가는 경우에는,
# 사이트 입장에서는 사이트가 부하가 될 수 있고, 정보를 뺏길 수 있기 때문에 그런 정보를 확인해서 접속을 차단할 수 있음 

# import requests
# url = "http://nandocoding.tistory.com"
# res = requests.get(url)
# res.raise_for_status()

# with open("nadocoding.html", "w", encoding="utf-8") as f:
#     f.write(res.text)

# 위에 사이트를 접속할 때 제한이 됨(이렇게 웹스크래핑이 아니라, 일반 크롬 브라우저로 저 웹페이지를 접속하면 접속 됨)

# *User agent 먼저 확인하기
# 'user agent string' 구글링-> 'What is my user agent?-~~'페이지 클릭-> 상단 파란박스에 나와있는 것이 브라우저 접속하는 자신의 user gent 정보!('Mozilla/5.0(~~~~'같은 것)
# 크롬에서 접속할 때와 익스플로러로 접속할 때 다르게 나올 것임-> 즉, 접속하는 브라우저에 따라 자신의 user agent가 다르게 나옴 ! 
# 그러므로, 서버 입장에서 user agent를 확인해서 정보를 다르게 보여줄 수 있음 
import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)

# 헤더 정보를 넣기 전에는 접속을 막았었는데, user agent를 넣어줌으로써 실제로 크롬 브라우저에서 접속했을 때와 동일한 결과를 받아오는 것을 알 수 있음!
