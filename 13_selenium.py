# #**22, 23 Selenium 기본 1,2

# # Selenium은 웹페이지 테스트 자동화를 할 수 있는 굉장히 유명한 framework 임!! 
# # 우리가 웹을 띄워서 어떤 페이지로 이동하고, 글자를 입력하고, 클릭 같은 것도 할 수 있는 이런 유용한 framework임
# # Selenium을 통해서 직접 웹브라우저를 컨트롤하면서(필요할 때는 클릭도 하고, 글자도 입력하고) html문서를 가져와서, 그 문서를 BeautifulSoup을 통해서 스크래핑작업을 할 수 있음
# # selenium은 '웹스크래핑' 강의에서는 가벼운 동작들에 대해서만 언급하고 지나갈 것임('업무자동화' 강의에서 깊이 다룸!)
# # 먼저, pip install selenium을 통해서 설치, 추가로 웹드라이버도 설치해야 함(웹드라이버는 브라우저마다 다름! 익스플로러용, 파일폭스용, 크롬용 등...)
# # 크롬으로 진행하기 때문에 크롬용 드라이버 설치!(호환이 되어야 하기 때문에, PC에 설치되어있는 크롬버전확인->그에 상응하는 버전의 드라이버 설치)
# # chromedriver 구글랑-> https://chromedriver.chromium.org/downloads 에서 크롬에서 확인한 버전과 같은 버전 드라이버 다운로드(다운로드한 'chromedriver.exe'파일을 작업하고 있는 'Python Workspace'파일 안에 넣기)

# # (먼저 파이썬 소스코드창 말고 터미널창에서 작업_터미널에서 한 내용(터미널 창에서 'python' 입력 이후))
# from selenium import webdriver

# browser = webdriver.Chrome() # 같은 파일에 있어서 ()만 쓴 것! 원래는 'Chrome()'의 괄호 안에 경로를 써줘야 함 ex)Chrome("c:/downloads/chromedriver.exe") 이런식으로. 
# browser.get("http://naver.com") # 네이버 접속

# #* 네이버 로그인버튼 클릭 해보기(*by_class_name)
# elem = browser.find_element_by_class_name("link_login") # 로그인버튼 엘리먼트의 class 이름을 통해서 찾음(BeautifulSoup에서와 비슷하게 find함수 사용)
# elem # (찾은 로그인버튼 엘리먼트 보여줌)
# elem.click() # 로그인버튼 엘리먼트 클릭(->로그인창으로 바뀜)
# browser.back() # back()-다시 이전 페이지로 돌아감
# browser.forward() # forward()-앞페이지로 넘어감
# browser.refresh() # refresh()-새로고침
# browser.back()

# #* 네이버 검색해보기(글자도 입력하고, 엔터도 치고)(*by_id)
# elem = browser.find_element_by_id("query") # 검색칸 엘리먼트의 id를 통해서 찾음
# elem
# # (Keys.ENTER 하기 위해서는 selenium 에서 다른 모듈을 써야 함, 참고: 글자를 입력하는것은 이 모듈 없이도 사용가능)
# from selenium.webdriver.common.keys import Keys
# elem.send_keys("나도코딩") # 검색칸에 "나도코딩" 입력 (글자를 입력하는 것은 바로 위에서 불러온 모듈 없이도 사용가능)
# elem.send_keys(Keys.ENTER) # 엔터기능(위에서 불러온 모듈로 인해 Keys.ENTER를 사용할 수 있음)

# #* 네이버에서 태그로 정보를 가져오기 (*by_tag_name)
# elem = browser.find_element_by_tag_name("a") # 웹페이지에서 처음 발견된 a태그 가져오기
# elem = browser.find_elements_by_tag_name("a") # 웹페이지에서 a태그 모두 가져오기 (element->elements 로 변경!)
# for e in elem:
#     e.get_attribute("href") # 참고: BeautifulSoup에서는 ["href"] / Selenium에서는 ("href")

# #* 다음에서 글자입력하고, 찾기 버튼 클릭해보기(*by_xpath)
# browser.get("http://daum.net")
# elem = browser.find_elemnet_by_name("q") # 검색칸 element를 name을 통해서 찾음
# elem
# elem.send_keys("나도코딩")
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") # 찾기버튼을 xpath로 찾음
# elem.click() # 찾기버튼을 클릭함

# # ==> 이런식으로 find 함수사용하면서 class 이름, id, tag, name, xpath 등을 통해 element를 찾아서 가져올 수 있음!

# #* 지금까지의 작업을 종료하고 브라우저를 종료하려면
# browser.close() #-> 현재 열려있는 탭만 종료
# browser.quit() #-> 브라우저 전체를 종료(브라우저에 탭이 몇 개가 떠있든 상관없이) 
# #(* exit() 하고 터미널에서 파이썬 종료시킴)


#**24 Selenium 심화(네이버 로그인)
import time # (로딩때문에)다음 작동이 원활하게 이루어지기 위해 time.sleep()을 사용하기 위해 import time을 써줌
from selenium import webdriver
browser = webdriver.Chrome() # 같은 파일 내에 있으므로 Chrome 뒤에 괄호만 써도되고, 괄호 안에 ("./chromedriver.exe") 이렇게 써줘도 무관

# 1.네이버 이동
browser.get("http://naver.com")
# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()
# 3. 아이디와 패스워드 입력
browser.find_element_by_id("id").send_keys("naver_id") # 개발자도구로 보니 id입력 칸이 id가 "id"인 input태그임. 찾아서 아이디 입력
browser.find_element_by_id("pw").send_keys("password") # id가 "pw"인 input태그 찾아서 패스워드 입력
# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3) # 3초 기다리고 다음 동작 하게 함-(로딩으로 다음 작동안할 경우 타임슬립 이용) 

# 5. 아이디 새로 입력
browser.find_element_by_id("id").clear() # id가 "id"인 element 값의 글자를 지워줌
browser.find_element_by_id("id").send_keys("my_id") # 지워진 칸에 다시 "my_id" 값 입력
#(실제 아이디와 패스워드 잘 입력해서 로그인했다고 가정하고)
# 6. html 정보 출력
print(browser.page_source) # 지금 페이지에 있는 모든 html 문서를 그대로 출력해줌
# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료
