# IF문

x = -1

if x > 0:
    print("값이 0보다 큽니다!!")
else:
    print("값이 음수입니다")


y = 3
if y >= 10:
    print("값이 10보다 큽니다")
elif y >= 0:
    print("값이 0 이상 10 미만입니다")
else:
    print("값이 음수입니다")

z = 7
"0 이상" if z >= 0 else "음수"


a = 3
b = 5


# While문

num = 1

# while num < 5:
#     print(num)
#     num = num + 1


while num < 10:
    if num % 2 == 0:
        print(f"{num} 은 짝수입니다")
    num = num + 1

money = 1000
while True:  # while True는 무한 반복이다
    money = money - 100
    print(f"잔액은 {money}원 입니다!")

    if money <= 0:
        break

# For 문
var = [1, 2, 3]

for i in var:
    print(i)


var1 = [10, 15, 17, 20]

for i in var1:
    if i % 2 == 0:
        print(f"{i}는 짝수입니다!!")
    else:
        print(f"{i}는 홀수입니다")

print(range(10))  # 0 1 2 3 4 5 6 7 8 9

for i in range(5):
    print(i)


a = [1, 2, 3]
result = []
for i in a:
    result.append(i**2)  # ** 제곱
print(result)  # [1,4,9]
result = [i**2 for i in a]  # [실행 for 변수 in 리스트 ]
print(result)

####### 페이지 36
