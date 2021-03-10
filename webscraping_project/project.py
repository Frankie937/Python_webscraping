#** 34 프로젝트 (-'나만의 비서' 프로그램 만들기)
#-> 네이버 날씨, 헤드라인 뉴스(네이버 뉴스) top3, IT 일반 뉴스(네이버 뉴스)top3, 오늘의 영어회화(해커스 영어)

#** 35, 36, 37, 38 네이버 날씨/헤드라인 뉴스/IT 일반 뉴스/오늘의 영어회화
import re  
import requests
from bs4 import BeautifulSoup


def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup # 이 create_soup 함수를 soup 객체로 반환 한다는 의미 

def print_news(index, title, link):
    print("{}. {}".format(index+1, title))
    print("  (링크 : {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
   
    # 오늘 날씨 정보 
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 현재온도, 최저/최고 기온
    curr_temp  = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "") # 현재온도
    min_temp = soup.find("span", attrs={"class":"min"}).get_text() # 최저 기온
    max_temp = soup.find("span", attrs={"class":"max"}).get_text() #최고 기온
    # 강수확률(오전/오후)
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip() # 오전 강수확률
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip() # 오후 강수확률
    # 미세먼지/초미세먼지
    dust = soup.find("dl", attrs={"class":"indicator"}).find_all("dd")
    pm10 = dust[0].get_text() # 미세먼지
    pm25 = dust[1].get_text() # 초미세먼지

    #출력
    print(cast)
    print("현재 {0} (최저 {1} / 최고 {2})".format(curr_temp, min_temp, max_temp))
    print("오전 {0} /오후 {1}".format(morning_rain_rate, afternoon_rain_rate))
    print() # 줄바꿈
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print() 


def scrape_headline_news():
    print("[헤드라인뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)

    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) # limit=3->조건에 해당되는 li 태그들 중에서 3개만 찾으라는 의미 
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip() # 'title = news.div.a.get_text().strip()' 해도 됨
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()

    # #혼자 해본 것(바로위의 'for문'만 제외하고 돌려보기)
    # top1 = news_list[0].find("a").get_text().strip()
    # top1_link = news_list[0].find("a")["href"]
    # top2 = news_list[1].find("a").get_text().strip()
    # top2_link = news_list[1].find("a")["href"]
    # top3 = news_list[2].find("a").get_text().strip()
    # top3_link = news_list[2].find("a")["href"]
    # # 출력
    # print("1. {}".format(top1))
    # print(" (링크 :","https://news.naver.com"+top1_link+")")
    # print("2. {}".format(top2))
    # print(" (링크 :","https://news.naver.com"+top2_link+")") 
    # print("3. {}".format(top3))
    # print(" (링크 :","https://news.naver.com"+top3_link+")")

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)

    new_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for index, news in enumerate(new_list):
        a_idx = 0 # img 태그 없을 경우 0번째 a 태그의 정보를 사용
        img = news.find("img")
        if img:
            a_idx = 1 # img태그가 있으면 1번째 a 태그의 정보를 사용
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url)

    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # setences(리스트형태)에 8문장이 있다고 가정할 때, index 기준 4~7까지 반으로 나눠서 가져옴(슬라이싱)
        print(sentence.get_text().strip())
    print()
    print("(한글 지문")
    for sentence in sentences[:len(sentences)//2]: # setences(리스트형태)에 8문장이 있다고 가정할 때, index 기준 0~3까지 반으로 나눠서 가져옴(슬라이싱)
        print(sentence.get_text().strip())
    print()


    #---- 내가 한 것(soup = create.soup(url) 이후 부터)----
    # box = soup.find_all("div", attrs="conv_txt")

    # englishs = box[1].find_all("span", attrs={"class":"conv_sub"})
    # print("(영어표현)")
    # for english in englishs:
    #     eng = english.get_text()
    #     print(eng)
    
    # print("(한글지문)")
    # koreans = box[0].find_all("span", attrs={"class":"conv_sub"})
    # for korean in koreans:
    #     kor = korean.get_text()
    #     print(kor)



if __name__ == "__main__": # 이 프로젝트를 직접 실행할 때는 밑에 구문이 동작되지만 다른 파일에서 호출될 때에는 실행되지 않음
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기 
    scrape_english() # 오늘 영어 회화 정보 가져오기 
