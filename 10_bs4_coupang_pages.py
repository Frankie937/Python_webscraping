#**14 BeautifulSoup4 활용 2-4 (쿠팡)
# 쿠팡에서 (1페이지만이 아니라) 1페이지부터 5페이지까지 검색된 노트북 중에서 조건에 맞는 노트북만 빼오도록 하기!
# 그리고 '9_bs4_coupang.py'파일에서 보다 더 보기 쉽게 만들기
import requests 
import re
from bs4 import BeautifulSoup
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

for i in range(1,6): # range(1,6)-> 1~5까지의 정수 
    # print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml") 

 
    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    
    for item in items:
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("  <광고 제품은 제외합니다.>  ")
            continue # (continue를 사용했기 때문에)광고제품인 경우에는 밑에 구문들 실행하지 않고, 바로 다음 item으로 넘어가게 됨
        
        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
        # 애플제품 제외
        if "Apple" in name:
            # print("  <애플 제품은 제외합니다.>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격

        # 리뷰(평점수) 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class":"rating"})  #평점(리뷰가 없을 수도 있기 때문 )
        if rate: # rate의 값이 있으면
            rate  = rate.get_text()
        else: #rate의 값이 없으면 
            # print("  <평점 없는 상품 제외합니다.>")
            continue

        rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점 수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            print("  <평점 수 없는 상품 제외합니다.>")
            continue
        # 제품링크(바로가기) 만들기
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) > 4.5 and int(rate_cnt) >= 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("http://www.coupang.com" + link))
            print("-"*100) # 제품마다 줄긋기
  
        



