import pandas as pd

# ! 셀레니움 명령어 - 브라우저

# ? webdriver.Chrome() : 브라우저 열기
# ? driver.close() : 현재 탭 닫기
# ? driver.quit() : 브라우저 닫기
# ? driver.back() : 뒤로가기
# ? driver.forward() : 뒤로가기

# ! 셀레니움 명령어 - 엘리먼트 접근
# ? By.ID : 태그의 아이디값 으로 추출
# ? By.NAME : 태그의 네임으로 추출
# ? By.XPATH : 태그의 xpath로 추출
# ? By.LINK_TEXT : 태그의 링크로 추출
# ? By.TAG_NAME : 태그명으로 추출
# ? By.CLASS_NAME : 클래스명으로 추출
# ? By.CSS_SELECTOR : CSS선택자로 추출

# ! 셀레니움 명령어 - 동작
# ? .click() - 엘리먼트 클릭
# ? .clear() - 텍스트 삭제
# ? .send_keys(text) - 텍스트 입력
# ? .send_keys(Keys.CONTROL + "v") : 컨트롤+v 누르기

# ! 셀레니움 명령어 - 자바스크립트 실행
# ? execute_script()

# ! 정규표현식
# 크롤링한 결과물이 다음과 같다면
import re

data = "동 기업의 매출액은 전년 대비 29.2% 늘어났습니다"
# @ 여기에서 29.2% 만 추출하고 싶다면 [숫자.숫자% 정규표현식 = "\d+.\d+%"]
filtered_data = re.findall("\d+.\d+%", data)
print(filtered_data)

# ! 메타문자
# ? \d , [0~9] 숫자와 매치
# ? \D , 숫자가 아닌것과 매치
# ? \s , [^\t\n\r\f\v]  공백문자와 매치
# ? \S , 공백이 아닌 문자와 매치
# ? \w , [a~zA-Z0~9] , 문자+숫자
# ? \W , 문자+숫자가 아닌것과 매치
# ? .  , 줄바꿈 문자인 \n을 제외한 모든 문자와 매치 - a.e는 a+모든문자+e 의미
# ? a[.]e , 문자그대로 a.e를 나타냄
# ? *  , 반복문을 나타냄 ca*t의 의미는 ct, cat, caat, caaat, caaaat.........

# ! 정규식을 이용한 문자열 검색
# ? match() : 시작 부분부터 일치하는 패턴
# ? search() : 첫번째 일치하는 패턴
# ? findall() : 일치하는 모든 패턴
# ? finditer() : findall과 같지만 반복 가능한 객체 반환

# @ match()
p = re.compile("[a-z]+")  # 정규 표현식을 컴파일을 통해 변수에 저장
print(type(p))
# <class 're.Pattern'>
print(p.match("python"))
# <re.Match object; span=(0, 6), match='python'>
print(p.match("Use python"))  # 대문자가 들어가서 정규식과 매치되지 않는다
# None
print(p.match("PYTHON"))
# None

p = re.compile("[가-힣]+")
print(p.match("파이썬"))
# <re.Match object; span=(0, 3), match='파이썬'>

# @ Search() - 첫번째 일치하는 패턴 찾기
p = re.compile("[a-z]")
print(p.search("python"))
# <re.Match object; span=(0, 1), match='p'>

print(p.search("Use python"))
# <re.Match object; span=(1, 2), match='s'>

# @ findall()
p = re.compile("[a-zA-Z]+")
print(p.findall("Life is too short, Tou nedd Python."))
# ['Life', 'is', 'too', 'short', 'Tou', 'nedd', 'Python']

# @ finditer()
p = re.compile("[a-zA-Z]+")
m = p.finditer("Life is too short, Tou need Python")
print(m)
# <callable_iterator object at 0x1248c0e20> 반복 가능한 객체 출력
for i in m:
    print(i)
# <re.Match object; span=(0, 4), match='Life'>
# <re.Match object; span=(5, 7), match='is'>
# <re.Match object; span=(8, 11), match='too'>
# <re.Match object; span=(12, 17), match='short'>
# <re.Match object; span=(19, 22), match='Tou'>
# <re.Match object; span=(23, 27), match='need'>
# <re.Match object; span=(28, 34), match='Python'>

num = """r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t15\r\n\t\t\t\t\t23\r\n\t\t\t\t\t\t29\r\n\t\t\t\t\t\t34\r\n\t\t\t\t\t\t40\r\n\t\t\t\t\t\t44\r\n\t\t\t\t\t\t"""

p = re.compile("[0-9]+")  # 숫자 부분만 찾아라
print(p.findall(num))
# ['15', '23', '29', '34', '40', '44']

dt = "> 오늘의 날짜는 2022.12.31 입니다"
p = re.compile("[0-9]+.[0-9]+.[0-9]+")
print(p.findall(dt))
# ['2022.12.31']

p = re.compile("[0-9]+")
m = p.findall(dt)
print(m)
# ['2022', '12', '31']
print("".join(m))
# 20221231
