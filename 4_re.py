import re # '정규식' 라이브러리 갖다 쓴다는 의미 

# # 4자리 문자로 형성된 차량번호라고 가정
# # ca?e 만 봄 3번째 문자는 못봤다고 가정할 때, 어떻게 찾을까? 
# # 정규식을 이용하여 찾아보자

# # p에 패턴을 정해줘야 함->'compile'함수 사용해서 어떤 정규식을 compile 할 지 ()안에 정해주기
# p = re.compile("ca.e")
# # . (ca.e): 하나의 문자를 의미(한 글자만) > care, cafe, case
# # ^ (^de): 문자열의 시작 > desk, destination
# # $ (se$): 문자열의 끝 > case, baese

# # p에게 정규식 값을 받아왔으니 이 p와 매칭되는지 봐야 함-> 'match'라는 함수 사용(비교할려는 값을 ()괄호 안에 넣어주기)
# m = p.match("case") # 매칭된 값을 m에 받아와서 
# print(m.group()) # 정규식과 매칭되면 case를 출력해줌 
# m = p.match("caffe") 
# print(m.group()) # 정규식과 매칭되지 않으면 에러 발생 

# # 매칭이 되었을 경우에만 출력하는 코드 작성
# p = re.compile("ca.e")
# m = p.match("case")
# if m:
#     print(m.group()) # 매칭되는 경우 비교값인 case 출력
# else: 
#     print("매칭되지 않았습니다. ") # 매칭되지 않을 경우 이 문구 출력

# 위에 부분을 그냥 함수로 처리!!
p = re.compile("ca.e")
def print_match(m): 
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열 반환(string은 변수이기 때문에 괄호 없이 사용)
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index 반환
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index 반환
        print("m.span()", m.span()) # 일치하는 문자열의 시작과 끝 index 반환
    else: 
        print("매칭되지 않았습니다. ") 

m = p.match("good care") # *match함수: 주어진 문자열의 처음부터 일치하는지 확인 
print_match(m) # careless를 값으로 넣어주면 'print(m.group())'에서는 care로 나옴("good care"값을 넣어주면 바로 매칭되지 않았다고 출력됨) 

m = p.search("good care") # *search함수: 주어진 문자열 중에 일치하는 게 있는지 확인
print_match(m) # good care 값을 넣어주면 'print(m.group())'에서는 care로 나옴(careless를 값으로 넣어줘도 care로 잘 출력됨)

# lst = p.findall("good care cafe") # *findall: 일치하는 모든 것을 리스트 형태로 반환 ['care', 'cafe'] 이렇게 
# print(lst)

# 정규식을 정리하면
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인 
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환 

# "원하는 형태" : 정규식 
# . (ca.e): 하나의 문자를 의미(한 글자만) > care, cafe, case
# ^ (^de): 문자열의 시작 > desk, destination
# $ (se$): 문자열의 끝 > case, baese

# 정규식을 더 공부하고 싶으면 w3school 홈페이지-> 하단에 python(learn python)클릭-> 왼쪽 list 중에 'Python RegEx'클릭해서 공부하면 됨
# 또는, python re 구글링해서 're---Regular expression operations---Python' 페이지(파이썬 공식홈페이지) 클릭해서 공부하면 됨
