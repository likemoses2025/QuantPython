import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rc("font", family="AppleGothic")
import matplotlib as mpl


# @ 가져올 수 있는 샘플 데이터셋 확인하기
dataset_names = sns.get_dataset_names()
print(dataset_names)

# @ 다이아몬드 샘플데이터 가져오기
df = sns.load_dataset("diamonds")
print(df.head())
#    carat      cut color clarity  depth  table  price     x     y     z
# 0   0.23    Ideal     E     SI2   61.5   55.0    326  3.95  3.98  2.43
# 1   0.21  Premium     E     SI1   59.8   61.0    326  3.89  3.84  2.31
# 2   0.23     Good     E     VS1   56.9   65.0    327  4.05  4.07  2.31
# 3   0.29  Premium     I     VS2   62.4   58.0    334  4.20  4.23  2.63
# 4   0.31     Good     J     SI2   63.3   58.0    335  4.34  4.35  2.75

# ? carat vs price
df.plot.scatter(x="carat", y="price", figsize=(10, 6), title="캐럿과 가격 간의 관계")
plt.show()

# ? cut별로 색상 적용하기 ( c변수에 색깔로 표현하고 싶은 열, cmap에 파레트를 지정)
df.plot.scatter(x="carat", y="price", c="cut", cmap="Set2", figsize=(10, 6))
plt.show()

# ? 히스토그램 갸격을 선택하고 hist 그래프로 표현
df["price"].plot.hist(figsize=(10, 6), bins=20)

# ? color에 따른 carat 평균 - color별로 그룹으로 묶은후 carat의 평균을 구한다.그리고 plot.bar를 통해 막대그래프 구현
df.groupby("color")["carat"].mean().plot.bar(figsize=(10, 6))
plt.show()
