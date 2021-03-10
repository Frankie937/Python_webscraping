#**31 Headless 크롬
# headless를 쓸 때 한 가지 주의할 점이 있음
# headless 크롬일 때, 따로 user agent를 설정해주지 않았을 경우 서버입장에서 막을 수 있음
# 그러므로 user agent 값을 설정해주어야 함-options.add_argument("user-agent=Mozilla~~~")

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # (보이지 않지만)백그라운드에서 도는 브라우저 크기 제공
# user agent 값 설정 추가
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

browser = webdriver.Chrome(options=options) 
browser.maximize_window()

# 자신의 크롬 user agent 출력하기 
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)


detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()

# selenium을 더 공부하고 싶으면, 'selenium with python' 구글링->  'https://selenium-python.readthedocs.io' 여기서 더 공부하기 



