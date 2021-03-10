# #**12 BeautifulSoup4 활용 1-1 (가우스 전자) 
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# 네이버 웹툰 전체목록 가져오기 
cartoons = soup.find_all("h6", attrs={"class":"title"}) # find_all함수는 조건에 해당하는 h6태그 모두 찾음(그냥 find 함수는 찾은 h6태그의 첫번째만 찾음)
#-> soup 객체의 전체 문서중에서 class명이 title인 h6태그를 모두 가져오게 됨
for cartoon in cartoons: 
    print(cartoon.get_text()) # 조건에 해당되는 h6태그의 text만 출력 

# 웹툰 가우스전자 관련 해서는 '8_bs4_gauss.py'파일에서 이어서 설명함
