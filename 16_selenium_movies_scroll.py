
#**28, 29, 30 Selenium 활용 2-2,3,4 (구글 무비)
# '15_selenium_movies.py'에서 영화 10개만 갖고 올 수 있었는데(구글 무비 페이지가 스크롤 내려야 영화들이 더 보이는 동적페이지라서)
# selenium을 이용해서 이러한 동적페이지에 대한 자료를 더 갖고 오게 만들겠음!

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

#* 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

# # * 지정한 스크롤 내리기(-> selenium에서 자바스크립트 코드를 실행할 수 있음)
# # 해상도 높이인 1080 위치로 스크롤 내리기
# # browser.execute_script("window.scrollTo(0,1080)") # (0,1080)-세로길이만 1080위치로 내리라는 의미 (참고: 1920X1080 -PC 해상도 가로길이x세로길이)
# # (보충설명: 바탕화면> 마우스 오른쪽클릭> 디스플레이 설정 메뉴에서 PC 해상도를 확인하 수 있음)
# browser.execute_script("window.scrollTo(0,2080)") # 2080위치까지 스크롤 내림 (0으로 하면 가장 위로 스크롤을 올림)

# #* 화면 가장 아래로 스크롤 내리기(현재 문서의 총 높이만큼 스크롤을 내리는 것)
# browser.execute_script("window.scrollTo(0, documnet.body.scrollHeight)")

#* 시간 간격을 두면서 '화면 가장 아래로 스크롤 내리기'를 반복
import time
interval = 2 # 2초에 한번씩 스크롤 내림(로딩이 더 걸리면 초를 더 늘려도 됨)
# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
# 반복 수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height
print("스크롤 완료")

#* 위에서 Selenium으로 가져온 웹페이지 문서를 bs4로 웹스크래핑 하는 작업(원래 import 코드 부분들은 맨위쪽에 다 적는데 수업이니깐 순서대로 진행해서 코드를 중간에 적음)
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml") # browser.page_source- selenium으로 구글무비 접속해서 스크롤을 맨 밑에까지 내린 html문서 정보를 가져옴 

# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]}) 리스트 형태로 집어넣을 수도 있음(그 값들에 해당되는 모든 element 가져옴)
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies)) # 200개 나옴

# 할인하는 영화만 갖고오도록 (총 200개 영화 중 할인된 영화 몇개만 나오게 함)
for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:  
        continue
    # 할인 후 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    # 링크정보
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크: "https://play.google.com"+link
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)

browser.quit()

