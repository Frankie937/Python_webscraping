#----내가 한 것----

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("https://www.daum.net/") # 다음 접속

elem = browser.find_element_by_class_name("tf_keyword") # 검색칸 엘리먼트 찾기 
elem.click()
elem.send_keys("송파 헬리오시티") # 입력
elem.send_keys(Keys.ENTER) #엔터

soup = BeautifulSoup(browser.page_source, "lxml")

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")

for idx, row in enumerate(data_rows, start=1): # start = 1 은 index를 1부터 시작하겠다는 의미 ("https://cafe.naver.com/funcc/53513" 참고)
    c1 = row.find("td", attrs={"class":"col1"}).get_text()
    c2 = row.find("td", attrs={"class":"col2"}).get_text()
    c3 = row.find("td", attrs={"class":"col3"}).get_text()
    c4 = row.find("td", attrs={"class":"col4"}).get_text()
    c5 = row.find("td", attrs={"class":"col5"}).get_text()

    print("============ 매물 {} ============".format(idx))
    print("거래 : " + c1)
    print(f"면적 : {c2} (공급/전용)")
    print(f"가격 : {c3} (만원)")
    print("동 : " + c4)
    print("층 : " + c5)

browser.quit()


#---나도 코딩----

import requests 
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=BFT&nil_profile=fix_similar&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# soup객체에 있는 내용을 가지고 html파일을 만든 다음에, 우리가 원하는 정보가 있는지 기본적으로 확인하고 웹스크래핑 해야 함!!
# (정보가 없다면 user-agent를 넣어보든지, 필요하다면 selenium을 사용해야 할 수 있기 때문)
# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify()) # 만든 파일에서 원하는 정보 찾아보기(있으면 받아온 웹페이지 문서를 가지고 바로 쓸 수 있다는 의미)

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("========== 매물 {} ==========".format(index+1))
    print("거래 :", columns[0].get_text().strip()) # strip()-> 불필요한 공백 제거 
    print("면적 :", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 :", columns[2].get_text().strip(), "(만원)")
    print("동 :", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())