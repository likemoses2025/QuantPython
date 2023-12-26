import seaborn as sns
import pandas as pd
import numpy as np

#! 그룹 연산하기
# 1. 분할 - split
# 2. 적용 - apply(Sum)
# 3. 결합 - combine

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

# @ 그룹 나누기 - species에 따라 데이터의그룹을 나눔 groupby()

df_group = df.groupby(["species"])
print(df_group)
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x165b04390>

print(df_group.head(2))
#        species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
# 0       Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
# 1       Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
# 152  Chinstrap      Dream            46.5           17.9              192.0       3500.0  Female
# 153  Chinstrap      Dream            50.0           19.5              196.0       3900.0    Male
# 220     Gentoo     Biscoe            46.1           13.2              211.0       4500.0  Female
# 221     Gentoo     Biscoe            50.0           16.3              230.0       5700.0    Male

for key, group in df_group:
    print(key)
    print(group.head(2))

# [6 rows x 7 columns]
# ('Adelie',)
#   species     island  bill_length_mm  ...  flipper_length_mm  body_mass_g     sex
# 0  Adelie  Torgersen            39.1  ...              181.0       3750.0    Male
# 1  Adelie  Torgersen            39.5  ...              186.0       3800.0  Female

# [2 rows x 7 columns]
# ('Chinstrap',)
#        species island  bill_length_mm  ...  flipper_length_mm  body_mass_g     sex
# 152  Chinstrap  Dream            46.5  ...              192.0       3500.0  Female
# 153  Chinstrap  Dream            50.0  ...              196.0       3900.0    Male

# [2 rows x 7 columns]
# ('Gentoo',)
#     species  island  bill_length_mm  ...  flipper_length_mm  body_mass_g     sex
# 220  Gentoo  Biscoe            46.1  ...              211.0       4500.0  Female
# 221  Gentoo  Biscoe            50.0  ...              230.0       5700.0    Male

# [2 rows x 7 columns]

# @ 그룹별 연산하기

# print(df_group.mean())
# print(df.groupby(["species", "sex"]))
# print(df.groupby(["species"]).agg(["max", "min"]))
