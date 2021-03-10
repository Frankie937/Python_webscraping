#**14 BeautifulSoup4 활용 2-1,2,3 (쿠팡)
import requests 
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# print(res.text) 
items = soup.find_all("li", attrs={"class":re.compile("^search-product"})
# print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("  <광고 제품은 제외합니다.>  ")
        continue # (continue를 사용했기 때문에)광고제품인 경우에는 아래의 구문들 실행하지 않고, 바로 다음 item으로 넘어가게 됨
    
    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    # 애플제품 제외
    if "Apple" in name:
        print("  <애플 제품은 제외합니다.>")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격

    # 리뷰(평점수) 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})  #평점(리뷰가 없을 수도 있기 때문에 if 구문 넣어줌)
    if rate: # rate의 값이 있으면
        rate  = rate.get_text()
    else: #rate의 값이 없으면 
        print("  <평점 없는 상품 제외합니다.>")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점 수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1] # rate_cnt의 text가 '(26)'으로 표시된 걸 '26'으로 바꿔주기 위해 슬라이싱 사용([1:-1]->위치 1부터 맨마지막 위치 앞까지) 
    else:
        print("  <평점 수 없는 상품 제외합니다.>")
        continue

    if float(rate) > 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)


