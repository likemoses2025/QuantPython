import seaborn as sns
import pandas as pd

#! 새로운 열 만들기
df = sns.load_dataset("mpg")
print(df)

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
