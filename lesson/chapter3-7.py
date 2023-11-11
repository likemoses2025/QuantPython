import seaborn as sns

#! 데이터 재구조화

df = sns.load_dataset("penguins")  # 팔머 팽귄의 3가지 종에 대한 데이터
print(df.head())

#   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
# 0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
# 1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
# 2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
# 3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
# 4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female

# ? melt() - 엑셀에서 행을 열로 변환하는 법
print(df.melt(id_vars=["species", "island", "sex"]))
#      species     island     sex        variable   value
# 0     Adelie  Torgersen    Male  bill_length_mm    39.1
# 1     Adelie  Torgersen  Female  bill_length_mm    39.5
# 2     Adelie  Torgersen  Female  bill_length_mm    40.3
# 3     Adelie  Torgersen     NaN  bill_length_mm     NaN
# 4     Adelie  Torgersen  Female  bill_length_mm    36.7
# ...      ...        ...     ...             ...     ...
# 1371  Gentoo     Biscoe     NaN     body_mass_g     NaN
# 1372  Gentoo     Biscoe  Female     body_mass_g  4850.0
# 1373  Gentoo     Biscoe    Male     body_mass_g  5750.0
# 1374  Gentoo     Biscoe  Female     body_mass_g  5200.0
# 1375  Gentoo     Biscoe    Male     body_mass_g  5400.0

# ? pivot_table() - 엑셀의 피벗테이블과 유사 4가지 값 (index,columns,values(데이터 값),aggfunc(데이터집계함수))
df_pivot1 = df.pivot_table(
    index="species", columns="island", values="bill_length_mm", aggfunc="mean"
)
print(df_pivot1)  # * 행 인덱스에는 species 열 인덱스에는 island 값은 bill_length_mm 집계함수는 mean(평균)
# island        Biscoe      Dream  Torgersen
# species
# Adelie     38.975000  38.501786   38.95098
# Chinstrap        NaN  48.833824        NaN
# Gentoo     47.504878        NaN        NaN

# ? pivot_table의 인덱스를 여러개 입력하는 법
df_pivot2 = df.pivot_table(
    index=["species", "sex"],
    columns="island",
    values=["bill_length_mm", "flipper_length_mm"],
    aggfunc=["mean", "count"],
)
print(df_pivot2)
#                  bill_length_mm                       flipper_length_mm              ... bill_length_mm           flipper_length_mm
# island                   Biscoe      Dream  Torgersen            Biscoe       Dream  ...          Dream Torgersen            Biscoe Dream Torgersen
# species   sex                                                                        ...
# Adelie    Female      37.359091  36.911111  37.554167        187.181818  187.851852  ...           27.0      24.0              22.0  27.0      24.0
#           Male        40.590909  40.071429  40.586957        190.409091  191.928571  ...           28.0      23.0              22.0  28.0      23.0
# Chinstrap Female            NaN  46.573529        NaN               NaN  191.735294  ...           34.0       NaN               NaN  34.0       NaN
#           Male              NaN  51.094118        NaN               NaN  199.911765  ...           34.0       NaN               NaN  34.0       NaN
# Gentoo    Female      45.563793        NaN        NaN        212.706897         NaN  ...            NaN       NaN              58.0   NaN       NaN
#           Male        49.473770        NaN        NaN        221.540984         NaN  ...            NaN       NaN              61.0   NaN       NaN

# ? stack() and unstack()
# * stack() : 열 인덱스를 행 인덱스로 변환
# * unstack() : 행 인덱스를 열 인덱스로 변환
df_pivot3 = df.pivot_table(
    index=["species", "sex"],
    columns=["island"],
    values="bill_length_mm",
    aggfunc="mean",
)
print(df_pivot3)
# island               Biscoe      Dream  Torgersen
# species   sex
# Adelie    Female  37.359091  36.911111  37.554167
#           Male    40.590909  40.071429  40.586957
# Chinstrap Female        NaN  46.573529        NaN
#           Male          NaN  51.094118        NaN
# Gentoo    Female  45.563793        NaN        NaN
#           Male    49.473770        NaN        NaN

# ? 열 인데스 island를 행 index로 바꿈
print("STACK", df_pivot3.stack())
# species    sex     island
# Adelie     Female  Biscoe       37.359091
#                    Dream        36.911111
#                    Torgersen    37.554167
#            Male    Biscoe       40.590909
#                    Dream        40.071429
#                    Torgersen    40.586957
# Chinstrap  Female  Dream        46.573529
#            Male    Dream        51.094118
# Gentoo     Female  Biscoe       45.563793
#            Male    Biscoe       49.473770
# dtype: float64

# ? 위의 데이터를 데이터프레임으로 변경하기
print(df_pivot3.stack().to_frame())
# species   sex    island
# Adelie    Female Biscoe     37.359091
#                  Dream      36.911111
#                  Torgersen  37.554167
#           Male   Biscoe     40.590909
#                  Dream      40.071429
#                  Torgersen  40.586957
# Chinstrap Female Dream      46.573529
#           Male   Dream      51.094118
# Gentoo    Female Biscoe     45.563793
#           Male   Biscoe     49.473770

# ? unstack()
print(df_pivot3.unstack())
# island        Biscoe                 Dream             Torgersen
# sex           Female       Male     Female       Male     Female       Male
# species
# Adelie     37.359091  40.590909  36.911111  40.071429  37.554167  40.586957
# Chinstrap        NaN        NaN  46.573529  51.094118        NaN        NaN
# Gentoo     45.563793  49.473770        NaN        NaN        NaN        NaN
