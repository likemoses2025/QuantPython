import seaborn as sns

#! 데이터 프레임에 함수 적용하기

# ? 시리즈에 함수 적용하기
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

bill_length_mm = df["bill_length_mm"]
print(bill_length_mm.head())
# 0    39.1
# 1    39.5
# 2    40.3
# 3     NaN
# 4    36.7
# Name: bill_length_mm, dtype: float64

# ? 제곱근 구하기  sqrt함수는 제곱근을 구해줌
import numpy as np

result = bill_length_mm.apply(np.sqrt)
print(result.head())
# 0    6.252999
# 1    6.284903
# 2    6.348228
# 3         NaN
# 4    6.058052


def mm_to_cm(num):
    return num / 10


result2 = bill_length_mm.apply(mm_to_cm)
print(result2.head())
# 0    3.91
# 1    3.95
# 2    4.03
# 3     NaN
# 4    3.67
# Name: bill_length_mm, dtype: float64

#! P94부터
