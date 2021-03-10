import requests
res = requests.get("http://naver.com") #-> 해당 주소에 접속에서 정보를 가져오겠다는 의미
# 실제로 웹페이지에 접속하려 할 때, 문제가 생길 수 있음(정보를 잘 받아왔는지, 페이지에 접속권한이 없는지, 페이지가 없는지 등)
# 그걸 확인하기 위해 '응답코드'를 찍을 수 있음(res.status_code 사용)
print("응답코드 :", res.status_code) # 값이 '200'나오면 정상적으로 작동했다는 의미('403'이 나오면 접속권한이 없다는 의미)
# 응답코드 관련 처리방법1
if res.status_code == requests.codes.ok: # 'requests.codes.ok'는 응답코드 '200'이라는 의미와 똑같은 의미
    print("정상입니다")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]" )
# 응답코드 관련 처리방법2
res.raise_for_status() # 웹스크래핑을 하기 위해서 올바로 코드를 가져왔다면 문제가 없고, 그렇지 않은 경우에는 에러를 표시
print("웹 스크래핑을 진행합니다.") # 문제가 없으면 이 문장 출력됨, 문제있으면 출력안되고 오류나서 프로그램 종료

# 그러므로, 이렇게 두 줄로 간단하게 처리 가능! 항상 이렇게 쌍으로 사용 
res = requests.get("http://google.com")
res.raise_for_status()

print(len(res.text)) # 우리가 가져온 html 문서의 글자 개수가 출력됨

with open("mygoogle.html", "w", encoding="utf8") as f:  # 가져온 html을 파일로 만들어 봄
    f.write(res.text) # 만든 파일에 가져온 himl 문서의 글자를 넣기 (열어보면 가져온 html과 거의 똑같이 나옴)


