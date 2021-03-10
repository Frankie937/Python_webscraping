#** 20 CSV 기본 1 (네이버 금융)

import csv # csv형태로 저장을 할꺼라서 csv모듈을 import 해옴
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

#엑세파일로 만들기 위한 작업코드 
filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") # newline=""을 넣는 이유는 불필요한 줄바꿈row를 없애기 위해 (안하면 각row마다 한줄씩 띄고 자료들이 들어감)
writer = csv.writer(f) #엑셀파일은 열때 encoding="utf-8"해도 한글이 깨질경우, encoding="utf-8-sig"을 해주면 됨!!

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") #탭으로 구분한 데이터들이 리스트로 들어감
# (이런식으로 title = ["N", "종목명", "현재가", ...] )
print(type(title)) #->list 형태라고 함 
writer.writerow(title) 

for page in range(1,5): # 1페이지~4페이지까지(1페이지에 주식이 50개씩 있음_총 200개 갖고오겠다는 것) 사용하니깐 range(1,5)
    res = requests.get(url + str(page)) # 괄호 안에 url+str(page) 대신에 그냥 url만 넣고 위에 있는 url 변수를 for문 안으로 들여보내서 끝에 {} 넣고 .format(page) 해도 상관없음
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 의미없는 데이터 skip(네이버금융페이지 보니, tr 안에 td들이 1개 이하로 있는 것들이 있음-그것은 그냥 줄바꿈을 위해 있는 코드기에)
            continue
        data = [column.get_text().strip() for column in columns] # 한 줄로 쓰는 for문 작성 방법 'i for i in lst' 그리고 []로 감싼 이유는 값들을 리스트 형태(','로 구분 ["값","값","값"])로 집어 넣기 위해서/strip()함수는 '\n','\t' 같은 불필요한 text 지우고 갖고 오기 위해 씀
        # print(data)
        writer.writerow(data) #writerow 괄호 안에는 리스트형태의 자료를 넣어주는 것('data'변수에는 리스트형태로 값들이 들어가 있음 그리고 ','로 구분 ["값","값","값"]))


