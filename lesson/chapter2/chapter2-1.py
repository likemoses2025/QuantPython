import datetime


var = datetime.datetime.now()
print(var)  # 2023-11-05 11:24:58.953788

print(type(var))  # datetime.datetime

print(var.year)  # 2023
print(var.month)  # 11
print(var.day)  # 5
print(var.hour)  # 11
print(var.minute)  # 24
print(var.second)  # 58
print(var.microsecond)  # 408487 백만분의 1초
print(var.weekday())  # 6  0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일

print(var.date())  # 2023-11-05
print(var.time())  # 11:24:58.953788


# 포멧바꾸기
## strftime : 시간 정보를 문자열로 바꿈
## strptime : 문자열을 시간 정보로 바꿈

print(var.strftime("%Y-%m-%d"))  # 2023-11-05

t = datetime.datetime(2022, 12, 31, 11, 59, 59)
print(t.strftime("%Y-%m-%d"))
print(t.strftime("%H시 %M분 %S초"))

t2 = datetime.datetime.strptime("2022-12-31 11:59:50", "%Y-%m-%d %H:%M:%S")
print("T2", t2, type(t2))  # T2 2022-12-31 11:59:50 <class 'datetime.datetime'>

# 날짜와 시간 연산하기
dt1 = datetime.datetime(2023, 12, 31)
dt2 = datetime.datetime(2022, 12, 31)
td = dt1 - dt2
print(td, type(td))  # 365 days, 0:00:00 <class 'datetime.timedelta'>


dt3 = datetime.datetime(2022, 12, 31)
print(dt3 + datetime.timedelta(days=1), type(dt3))


from dateutil.relativedelta import *

print("dateutil", dt1 + relativedelta(months=1))


# 코드를 일시정지 하기

import datetime
import time

for i in range(3):
    print(i)
    print(datetime.datetime.now())
    print("-----------------")
    time.sleep(2)  # 2초간 일시정지
