#**27 Selenium 활용 2-1 (구글 무비)
#-> 이번 내용은 동적 페이지(사용자가 어떤 동작을 했을 때 그때서야 동작하는 것)에 대한 웹스크래핑

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
# 웹스크래핑으로 접속시, 구글무비사이트가 미국페이지로 디폴트값으로 보내줌. 그러므로 아래 headers에서 "Accept-Language":"ko-KR,ko" 이 구문을 더추가
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language":"ko-KR,ko" # 한글 페이지가 있으면 한글 페이지로 보여달라는 의미 
}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})

print(len(movies)) # 10개 나옴 

# with open("movies.html", "w", encoding="utf-8") as f:
#     # f.write(res.text) # 파일 열어보면 코드가 빽빽하게 써져있음
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력해줌(파일 열어보면 위에꺼보다는 훨씬 코드가 정렬이 잘 되어 있음 )
#     # 파일을 열어보면 10개만 영화가 떠있음(그 이유는 페이지를 스크롤로 내려야 영화들이 더 나옴->즉, 이러한 페이지가 동적페이지!!)
#     # 그러므로 이러한 동적페이지에 대한 자료를 가져올 때 필요한 것이 selenium 이다. (10개말고 스크롤 끝까지 나오는 모든 영화 가져오도록) 

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)
    



