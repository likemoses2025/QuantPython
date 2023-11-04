# f string Formatting
name = "JangBuHo"
birth = "1977"

print("f string formatting",f'나의 이름은 {name}이며, {birth}년에 태어났습니다')

# 길이구함
a = "Life is too short"
print(len(a)) #17

# 문자열 치환
var2 = "퀀트 포트 폴리오 만들기"
var3 = var2.replace(" ", "_")
print(var3)

# 문자열 나누기
var10= "퀸트 투자 포트폴리오 만들기"
var11 = var10.split(" ")
print(var11)

# 문자열 인덱싱, 슬라이싱
str1 = "Quant"
print("인덱싱 2", str1[2])
print("인덱싱 -2", str1[-2])
print("인덱싱 0:3", str1[0:3])
print("인덱싱 :2", str1[:2])
print("인덱싱 3:", str1[3:])

################# page 14 ################################