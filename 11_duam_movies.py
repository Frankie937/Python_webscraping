#**18 BeautifulSoup4 활용 3-1,2 (다음 이미지)
import requests
from bs4 import BeautifulSoup


for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images): # enumerate 내장함수(순서가 있는 자료형을 입력받아서 인데스 값을 포함하는 enumerate 객체를 반환)
        #print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"): #startswith("//")-> '//'로 시작하는 값 이라는 의미 (개발자도구에서 보니, src값이 http로 완전하게 시작하는 것도 있지만, //로 시작하는 경우도 있기에)
            image_url = "https:" + image_url
        print(image_url)
        # for문으로 만들어진 각 url에 다시 접속해서 이미지를 파일로 저장하기 
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open("movie_{0}_{1}.jpg".format(year, idx+1), "wb") as f: # text가 아니기때문에 wb로 해야 함
            f.write(image_res.content) # content는 image_res가 가지고 있는 내용을 파일에 쓰겠다는 의미 (이미지라서 text대신 content 쓰는 것)
        
        if idx >= 4: # 상위 5개 영화 이미지만 다운로드 하기 위해 
            break

