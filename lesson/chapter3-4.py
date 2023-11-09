import pandas as pd

#! merge() 함수 - inner join, left join , right join , outer join

df1 = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)

df2 = pd.DataFrame(
    {
        "key": ["K0", "K1", "K3", "K4"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
# ? inner join - 교집합 리턴
result1 = pd.merge(df1, df2, on="key")
result2 = pd.merge(df2, df1, on="key")
print(result1)
print(result2)
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K3  A3  B3  C2  D2

#   key   C   D   A   B
# 0  K0  C0  D0  A0  B0
# 1  K1  C1  D1  A1  B1
# 2  K3  C2  D2  A3  B3

# ? left join - 윈쪽 프레임은 유지 되고 오른쪽 프레임이 키를 기준으로 합쳐짐
result3 = pd.merge(df1, df2, on="key", how="left")
print(result3)
#   key   A   B    C    D
# 0  K0  A0  B0   C0   D0
# 1  K1  A1  B1   C1   D1
# 2  K2  A2  B2  NaN  NaN
# 3  K3  A3  B3   C2   D2

# ? right join - 오른쪽 프레임은 유지 되고 왼쪽 프레임이 키를 기준으로 합쳐짐
result4 = pd.merge(df1, df2, on="key", how="right")
print(result4)
#   key    A    B   C   D
# 0  K0   A0   B0  C0  D0
# 1  K1   A1   B1  C1  D1
# 2  K3   A3   B3  C2  D2
# 3  K4  NaN  NaN  C3  D3

# ? outer join - 한쪽만 속하더라도 상관없이 합집합 부분을 리턴
result5 = pd.merge(df1, df2, on="key", how="outer")
print(result5)
#   key    A    B    C    D
# 0  K0   A0   B0   C0   D0
# 1  K1   A1   B1   C1   D1
# 2  K2   A2   B2  NaN  NaN
# 3  K3   A3   B3   C2   D2
# 4  K4  NaN  NaN   C3   D3

left2 = pd.DataFrame(
    {
        "key_left": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
right2 = pd.DataFrame(
    {
        "key_right": ["K0", "K1", "K3", "K4"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

# ? left join 키가 다른 경우
result6 = pd.merge(left2, right2, left_on="key_left", right_on="key_right", how="inner")
print(result6)
#   key_left   A   B key_right   C   D
# 0       K0  A0  B0        K0  C0  D0
# 1       K1  A1  B1        K1  C1  D1
# 2       K3  A3  B3        K3  C2  D2

# ? 더욱 직관적인 표현 inner는 교집합
result7 = left2.merge(right2, left_on="key_left", right_on="key_right", how="inner")
print(result7)
#   key_left   A   B key_right   C   D
# 0       K0  A0  B0        K0  C0  D0
# 1       K1  A1  B1        K1  C1  D1
# 2       K3  A3  B3        K3  C2  D2

import seaborn as sns
import pandas as pd

#! 새로운 열 만들기
df = sns.load_dataset("mpg")

df["ratio"] = (df["mpg"] / df["weight"]) * 100
print(df.head())


import numpy as np

num = pd.Series([-2, -1, 1, 2])
print(num)
# 0   -2
# 1   -1
# 2    1
# 3    2

print(np.where(num >= 0))  # * (값이 True인 인덱스를 반환 : ,)
#  array([2, 3], dtype=int64)

print(np.where(num >= 0, "양수", "음수"))  # * 조건을 만족하면 "양수" 불만족하면 "음수"
# ['음수' '음수' '양수' '양수']

# ? 여러 조건식 계산 horsepower >100 , >=100 , 200>=
df["horsepower_div"] = np.where(
    df["horsepower"] < 100,
    "100미만",
    np.where(
        df["horsepower"] >= 100,
        "100이상",
        np.where(df["horsepower"] >= 200, "200 이상", "기타"),
    ),
)
print(df.head(8))
#     mpg  cylinders  displacement  horsepower  weight  acceleration  model_year origin                       name     ratio horsepower_div
# 0  18.0          8         307.0       130.0    3504          12.0          70    usa  chevrolet chevelle malibu  0.513699          100이상
# 1  15.0          8         350.0       165.0    3693          11.5          70    usa          buick skylark 320  0.406174          100이상
# 2  18.0          8         318.0       150.0    3436          11.0          70    usa         plymouth satellite  0.523865          100이상
# 3  16.0          8         304.0       150.0    3433          12.0          70    usa              amc rebel sst  0.466065          100이상
# 4  17.0          8         302.0       140.0    3449          10.5          70    usa                ford torino  0.492896          100이상
# 5  15.0          8         429.0       198.0    4341          10.0          70    usa           ford galaxie 500  0.345543          100이상
# 6  14.0          8         454.0       220.0    4354           9.0          70    usa           chevrolet impala  0.321543          100이상
# 7  14.0          8         440.0       215.0    4312           8.5          70    usa          plymouth fury iii  0.324675          100이상

# ! 80쪽부터 시작
