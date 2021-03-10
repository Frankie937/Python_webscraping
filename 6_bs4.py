#**10 BeatuifulSoup4 기본1 네이버 웹툰
# pip install 이용하여 beautifulsoup4, lxml 설치 
# beautifulsoup4은 실제로 스크래핑 하기 위해서 사용되는 패키지
# lxml은 어떤 구문을 분석하기 위한 파써라는 것   

import requests 
from bs4 import BeautifulSoup
url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #res.text로 우리가 가져온 html 문서를 lxml 파써를 통해서 BeautifulSoup 객체로 만든 것
# # 그러면, soup 이라는 변수가 모든 정보를 다 가지고 있음
# print(soup.title)
# print(soup.title.get_text()) # title의 텍스트만 갖고옴 
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력(soup은 지금 가져온 html의 모든 문서를 갖고 있는데 그중에서 첫번째로 발견되는 a태그에 대한 정보를 갖고와줘 라는 것)
# print(soup.a.attrs) # a element의 속성 정보를 출력 (a태그에 해당 속성과 값들이 딕셔너리로 출력됨)
# print(soup.a["href"]) # a element의 href 속성 '값' 정보를 출력(원하는 속성의 값만 출력됨)

# # 웹스크래핑할 대상 문서에 대해 잘 모를 경우 find 함수 사용!! (위의 경우는 잘 알고 있을 때 가능한 방법)
# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # class="Nbtn_upsload"인 a element를 찾아줘(soup객체 모든 내용 중에서 attrs의 조건에 해당되는 첫 번째 a 태그를 가져옴)
# print(soup.find(attrs={"class":"Nbtn_upload"})) # class="Nbtn_upsload"인 어떤 element를 찾아줘(a태그인건 div태그이건 상관없음! 지정되지 않았기 때문에 어떠한 태그든 조건에 해당되는 첫 번째 element 출력)

print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a) # soup을 통해서 발견한 객체를 rank1객체에 넣어주고 soup객체처럼 똑같이 함수 사용가능-> '.a'를 써서 그 객체 내의 a태그만 출력할 수 있음!

# #**11 BeautifulSoup4 기본2 네이버웹툰
# #BeautifulSoup에서도 부모자식관계 이용 가능
# # 형제sibling 로 가는 방법('next_sibling'/'previous_sibling' 사용) 
# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling) # next_sibling을 두번 넣어준 이유는 줄바꿈같은거 있어서 한 번만 넣어주면 나오지 않음
# rank2 = rank1.next_sibling.next_sibling 
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling 
# print(rank2.a.get_text())
# # 부모로 가는 방법 parent
# print(rank1.parent)
# # 위에서 next_sibing/previous_sibling 을 두 번 해야 하는 번거로움이 있어서 'find_next_sibing()'사용(다음sibling으로 가는데 괄호 안의 조건에 해당하는 것을 찾음)
# rank2 = rank1.find_next_sibling("li") # rank1기준으로 다음 sibling을 찾을 때 li인 것만 찾는 것(그러므로 줄바꿈 즉, 개행정보 안찍힘)
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())
# # rank1 기준으로 다음형제들 모두를 가져올 때 쓰는 방법 find_next_siblings 사용!('s'만 더 붙이기)
# print(rank1.find_next_siblings("li"))

# webtoon = soup.find("a", text="") # text=""에 해당되는 a 태그를 찾아줌 
# print(webtoon) # text=""에 해당되는 a 태그를 출력해줌 

