#**31 Headless 크롬
# 이전까지는 브라우저를 직접 띄우면서 웹스크래핑을 하곤 했는데, 그러다보니 메모리도 많이 잡아먹기도 하고, 속도가 좀 느린면이 있음
# 화면을 볼 필요도 없고 일반PC가 아니라 서버에 웹스크래핑 작업을 한다면, 굳이 브라우저를 띄우는 작업을 할 필요가 없음
# 그럴 때 Headless 기능을 쓸 수 있음
# Headless 크롬-> 크롬이 없는 크롬(크롬을 띄우지 않고 크롬을 쓸 수 있는)->백그라운드에서 동작하는 거라고 이해하면 됨

#'16_seleniume_movies_scroll.py'의 코드를 불러와서 조금만 추가 해주면 됨 (추가코드: 11-13번, 15번 줄)

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # (보이지 않지만)백그라운드에서 도는 브라우저 크기 제공
 
browser = webdriver.Chrome(options=options)
browser.maximize_window()

#* 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

#* 시간 간격을 두면서 '화면 가장 아래로 스크롤 내리기'를 반복
import time
interval = 2 # 2초에 한번씩 스크롤 내림(로딩이 더 걸리면 초를 더 늘려도 됨)
# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")
# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height = curr_height
print("스크롤 완료")
# 스크롤 다 되었을 때 눈에 보이진 않지만 백그라운드에서 도는 브라우저를 스크린샷 해서 파일로 저장할 수 있음
browser.get_screenshot_as_file("google_movie.png") 

#* 위에서 Selenium으로 가져온 웹페이지 문서를 bs4로 웹스크래핑 하는 작업(원래 import 코드 부분들은 맨위쪽에 다 적는데 수업이니깐 순서대로 진행해서 코드를 중간에 적음)
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml") # browser.page_source- selenium으로 구글무비 접속해서 스크롤을 맨 밑에까지 내린 html문서 정보를 가져옴 

# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]}) 리스트 형태로 집어넣을 수도 있음(그 값들에 해당되는 모든 element 가져옴)
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

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