# Error 처리

number = [1, 2, 3, "4", 5]

for i in number:
    try:
        print(i**2)
    except:
        print("Error at : " + i)


# tqdm() 함수를 이용한 진행 단계 확인
import time
from tqdm import tqdm

for i in tqdm(range(10)):
    time.sleep(0.1)


# 함수
def sqrt(x):
    res = x ** (1 / 2)
    return res


print(sqrt(4))  # 2.0


def multiply(x, y):
    res = x**y
    return res


print(multiply(x=2, y=3))  # 8
print(multiply(x=5, y=2))  # 25


def divide(x, n=2):
    res = x / n
    return res


print(divide(3))  # 1.5
print(divide(6, 3))  # 2


# Lambda function
# 함수명 = lambda 매개변수1,매개변수2,....:statement

divide_lam = lambda x, n: x / n
print(divide_lam(6, 3))  # 2.0

import selenium

print(dir(selenium))

# 함수와 메서드의 차이
print(sum([1, 2]))  # 3

import pandas as pd

df = pd.DataFrame({"x": [1, 2, 3]})
print(df)
df.info()
