#** 12-13 BeautifulSoup4 활용 1-1,2(가우스 전자)
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# # 만화 제목+링크 가져오기
# cartoons = soup.find_all("td", attrs={"class":"title"}) # find_all이므로 cartoons는 데이터타입이 리스트임 
# title = cartoons[0].a.get_text() # cartoons가 리스트 형태임(값이 여러 개여서)
# link = cartoons[0].a["href"]
# print(title, "https://comic.naver.com"+link, sep=" : ")
# # 페이지에 있는 만화 제목+링크 다 갖고오기 
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link, sep=":")

# 만화 평점 평균 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text() # 'rate = cartoon.strong.get_text()' 해도 됨
    print(rate)
    total_rates += float(rate) # rate가 get_text()로 갖고왔기 때문에 str타입임 그러므로 float타입(실수)으로 바꿔줌 (*참고: int타입-정수)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates/len(cartoons)) # cartoons는 리스트형태(값이 여러개이므로) 그러므로 리스트의 len() 값은 리스트 값들의 갯수

# 참고로 BeatuifulSoup은 한글 문서가 제공되고 있기 때문에 더 자세히 공부하고 싶고, 예제를 보고 싶으면 
# 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/' 이 사이트 참고!!(페이지 중간부분에 '이문서는 한국어번역가능~' 클릭)
# 예제 코드와 자세한 설명이 있기에 유용함!

#**(다른 설명)
# 파이썬은 인터프리트 언어이기 때문에 terminal에서 바로 실행 가능! (컴파일 언어는 못함! 컴퓨터가 읽도록 번역과정이 필요하기 때문)
# terminal 창에서 "python" 쓰고 엔터치면 터미널에서 바로 코드쓰고 엔터누르면 결과 바로바로 확인 가능
