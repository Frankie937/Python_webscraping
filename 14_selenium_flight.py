#**25, 26 Selenium 활용 1-1,2 (네이버 항공권)

from selenium import webdriver
# 로딩 시간이 길어져서(화면이 바뀌지 않아) 다음 동작의 엘리먼트를 못찾을 때 time.sleep()사용 안하고 다른 방법 위해서 필요
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화(크롬창을 띄운 다음 전체화면으로 키워줌)

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click() # link의 text로 태그를 찾음("가는날 선택" text로 가는날 선택 태그를 찾음)

# # 이번달 27일, 28일 선택-(이번달의 27(가는날)-28(오는날) 항공권)
# browser.find_elements_by_link_text("27")[0].click() # [0]->'이번달'의미(가는날, 오는날 달력 각각 공통 날짜가 있기 때문에 elements로 갖고와서 순번을 넣어주어야 함)
# browser.find_elements_by_link_text("28")[0].click() # [0]->'이번달'의미([1]은 '다음달' 의미)

# # 다음달 27, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() 
# browser.find_elements_by_link_text("28")[1].click()

# 이번달 27, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() 
browser.find_elements_by_link_text("28")[1].click() 

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# '항공권 검색' 클릭하고, 그 이후 나타나는 결과창에서 첫번째 결과 출력 
browser.find_element_by_link_text("항공권 검색").click()
# 위의 '항공권 검색' 로딩 시간이 길어져서(화면이 바뀌지 않아) 다음 동작의 엘리먼트를 못찾을 때 time.sleep()사용안하고(불필요한 시간낭비 가능성 있기에) 다른 방법으로 아래 try구문 필요
try : # (10초 안에 해당 엘리먼트를 찾는 경우(다음 동작 수행할 수 있도록))
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) # 브라우저에 대해 10초 동안 기다리는데(WebDriverWait(browser,10)), 어떤 element가 나올 때까지(until(EC.~~))기다리라는 의미(괄호 안에 튜플형태로 작성)
# (만약, 로딩이 10초 이상 걸리면 에러남 ->그러므로, 보통 try/finally 구문에 넣어서 사용함) 
# (By.XPATH 말고도 By.ID/CLASS_NAME/LINK_TEXT 등 사용 가능)
    print(elem.text) # (10초 전에 로딩이 끝나서 다음동작 실행됨)-첫번째 결과 출력
finally : # (로딩이 10초 이상 걸려서 에러날 경우 브라우저 전체 종료 시킴)
    browser.quit()

# # 첫번째 결과 출력 (위에 try 구문 안넣었을 경우에 적었던 코드)
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)

# 일반적으로 selenium을 쓸 때, 어떤 페이지에 대해서 로딩하는데 시간이 좀 걸린다 하면 위의 try 구문처럼 처리해주면 됨!!
# (위에 3개의 'from~import~' 구문들도)