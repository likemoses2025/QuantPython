import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#! 데이터 시각화

# @ Matplotlib - 한글 지원 안함

df = sns.load_dataset("penguins")
print(df)
#     species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
# 0    Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
# 1    Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
# 2    Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
# 3    Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
# 4    Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female
# ..      ...        ...             ...            ...                ...          ...     ...
# 339  Gentoo     Biscoe             NaN            NaN                NaN          NaN     NaN
# 340  Gentoo     Biscoe            46.8           14.3              215.0       4850.0  Female
# 341  Gentoo     Biscoe            50.4           15.7              222.0       5750.0    Male
# 342  Gentoo     Biscoe            45.2           14.8              212.0       5200.0  Female
# 343  Gentoo     Biscoe            49.9           16.1              213.0       5400.0    Male

plt.scatter(df["flipper_length_mm"], df["body_mass_g"])
plt.show()

df_group = df.groupby("species")["body_mass_g"].mean().reset_index()
# * species로 묶고 값으로 body_mass_g을 평균 계산하기 , reset_index() 메서드를 통해 데이터프레임 형태로 나타냄
print(df_group)
#      species  body_mass_g
# 0     Adelie  3700.662252
# 1  Chinstrap  3733.088235
# 2     Gentoo  5076.016260

plt.bar(x=df_group["species"], height=df_group["body_mass_g"])
plt.show()

plt.rc("font", family="AppleGothic")
plt.hist(df["body_mass_g"], bins=30)
plt.xlabel("Body Mass")
plt.ylabel("Count")
plt.title("펭귄의 몸무게 분포")
plt.show()


# @ 선그래프
df_unrate = pd.read_csv(
    "https://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv"
)
print(df_unrate.head())  # *미국의 실업자 데이터

#          DATE  VALUE
# 0  1948-01-01    3.4
# 1  1948-02-01    3.8
# 2  1948-03-01    4.0
# 3  1948-04-01    3.9
# 4  1948-05-01    3.5

df_unrate["DATE"] = pd.to_datetime(df_unrate["DATE"])  # DATE 열을 datetime객쳋로 변환
plt.plot(df_unrate["DATE"], df_unrate["VALUE"])  # X Y축 정보입력
plt.show()
