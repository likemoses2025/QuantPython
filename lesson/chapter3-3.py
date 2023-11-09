import pandas as pd

#! 데이터프레임 합치기

# ? concat()

df1 = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=[0, 1, 2, 3],
)

df2 = pd.DataFrame(
    {
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    },
    index=[4, 5, 6, 7],
)

df3 = pd.DataFrame(
    {
        "A": ["A8", "A9", "A10", "A11"],
        "B": ["B8", "B9", "B10", "B11"],
        "C": ["C8", "C9", "C10", "C11"],
        "D": ["D8", "D9", "D10", "D11"],
    },
    index=[8, 9, 10, 11],
)

union = pd.concat([df1, df2, df3])
print(union)
#       A    B    C    D
# 0    A0   B0   C0   D0
# 1    A1   B1   C1   D1
# 2    A2   B2   C2   D2
# 3    A3   B3   C3   D3
# 4    A4   B4   C4   D4
# 5    A5   B5   C5   D5
# 6    A6   B6   C6   D6
# 7    A7   B7   C7   D7
# 8    A8   B8   C8   D8
# 9    A9   B9   C9   D9
# 10  A10  B10  C10  D10
# 11  A11  B11  C11  D11

df4 = pd.DataFrame(
    {
        "B": ["B8", "B9", "B10", "B11"],
        "D": ["D8", "D9", "D10", "D11"],
        "F": ["F8", "F9", "F10", "F11"],
    },
    index=[2, 3, 6, 7],
)

union2 = pd.concat([df1, df4])
print("union2", union2)
# union2      A    B    C    D    F
#         0   A0   B0   C0   D0  NaN
#         1   A1   B1   C1   D1  NaN
#         2   A2   B2   C2   D2  NaN
#         3   A3   B3   C3   D3  NaN
#         2  NaN   B8  NaN   D8   F8
#         3  NaN   B9  NaN   D9   F9
#         6  NaN  B10  NaN  D10  F10
#         7  NaN  B11  NaN  D11  F11

# ? 행 인덱스 초기화
union3 = pd.concat([df1, df4], ignore_index=True)
print(union3)
#      A    B    C    D    F
# 0   A0   B0   C0   D0  NaN
# 1   A1   B1   C1   D1  NaN
# 2   A2   B2   C2   D2  NaN
# 3   A3   B3   C3   D3  NaN
# 4  NaN   B8  NaN   D8   F8
# 5  NaN   B9  NaN   D9   F9
# 6  NaN  B10  NaN  D10  F10
# 7  NaN  B11  NaN  D11  F11

# ? 열 기준으로 데이터 합치기
result = pd.concat([df1, df4], axis=1)
print(result)
#      A    B    C    D    B    D    F
# 0   A0   B0   C0   D0  NaN  NaN  NaN
# 1   A1   B1   C1   D1  NaN  NaN  NaN
# 2   A2   B2   C2   D2   B8   D8   F8
# 3   A3   B3   C3   D3   B9   D9   F9
# 6  NaN  NaN  NaN  NaN  B10  D10  F10
# 7  NaN  NaN  NaN  NaN  B11  D11  F11

# ? 두 데이터프레임이 공통으로 존재하는 행 인덱스 2,3을 기준으로 데이터가 합쳐집
result2 = pd.concat([df1, df4], axis=1, join="inner")
print(result2)
#     A   B   C   D   B   D   F
# 2  A2  B2  C2  D2  B8  D8  F8
# 3  A3  B3  C3  D3  B9  D9  F9

# ? 데이터 프레임에 시리즈 합치기
s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
print(s1)
# 0    X0
# 1    X1
# 2    X2
# 3    X3
result3 = pd.concat([df1, s1], axis=1)
print(result3)
#     A   B   C   D   X
# 0  A0  B0  C0  D0  X0
# 1  A1  B1  C1  D1  X1
# 2  A2  B2  C2  D2  X2
# 3  A3  B3  C3  D3  X3

import seaborn as sns

#! 인데스 다루기

df = sns.load_dataset("mpg")
print(df.head())

# * Index 필드를 Name으로 설정
print(df.set_index("name", inplace=True))
print(df.head())

# * 인덱스 정렬  / 오름차순
df.sort_index(inplace=True)
print(df.head())

# * 인덱스 정렬  / 내림차순
df.sort_index(inplace=True, ascending=False)
print(df.head())


# * 인덱스 초기화
df.reset_index(inplace=True)
print(df.head())


#! 필터링 -  불리언 인덱싱

df = sns.load_dataset("mpg")
print(df.tail(10))
#       mpg  cylinders  displacement  horsepower  weight  acceleration  model_year  origin                        name
# 388  26.0          4         156.0        92.0    2585          14.5          82     usa  chrysler lebaron medallion
# 389  22.0          6         232.0       112.0    2835          14.7          82     usa              ford granada l
# 390  32.0          4         144.0        96.0    2665          13.9          82   japan            toyota celica gt
# 391  36.0          4         135.0        84.0    2370          13.0          82     usa           dodge charger 2.2
# 392  27.0          4         151.0        90.0    2950          17.3          82     usa            chevrolet camaro
# 393  27.0          4         140.0        86.0    2790          15.6          82     usa             ford mustang gl
# 394  44.0          4          97.0        52.0    2130          24.6          82  europe                   vw pickup
# 395  32.0          4         135.0        84.0    2295          11.6          82     usa               dodge rampage
# 396  28.0          4         120.0        79.0    2625          18.6          82     usa                 ford ranger
# 397  31.0          4         119.0        82.0    2720          19.4          82     usa                  chevy s-10

# ? col 실린더 고유값 추출
print(df["cylinders"].unique())  # [8 4 6 3 5]

# ? 실린더 열의 값이 4인 값 필터링
filter_bool = df["cylinders"] == 4
print(filter_bool.tail(10))
# 388     True
# 389    False
# 390     True
# 391     True
# 392     True
# 393     True
# 394     True
# 395     True
# 396     True
# 397     True

# ? 실린더의 값이 4인 값 전체
print(df.loc[filter_bool,])
#       mpg  cylinders  displacement  horsepower  weight  acceleration  model_year  origin                          name
# 14   24.0          4         113.0        95.0    2372          15.0          70   japan         toyota corona mark ii
# 18   27.0          4          97.0        88.0    2130          14.5          70   japan                  datsun pl510
# 19   26.0          4          97.0        46.0    1835          20.5          70  europe  volkswagen 1131 deluxe sedan
# 20   25.0          4         110.0        87.0    2672          17.5          70  europe                   peugeot 504
# 21   24.0          4         107.0        90.0    2430          14.5          70  europe                   audi 100 ls
# ..    ...        ...           ...         ...     ...           ...         ...     ...                           ...
# 393  27.0          4         140.0        86.0    2790          15.6          82     usa               ford mustang gl
# 394  44.0          4          97.0        52.0    2130          24.6          82  europe                     vw pickup
# 395  32.0          4         135.0        84.0    2295          11.6          82     usa                 dodge rampage
# 396  28.0          4         120.0        79.0    2625          18.6          82     usa                   ford ranger
# 397  31.0          4         119.0        82.0    2720          19.4          82     usa                    chevy s-10

# ? 실린더의 값이 4 , 마력이 100
filter_bool2 = (df["cylinders"] == 4) & (df["horsepower"] >= 100)
# print(df.loc[filter_bool2, ["cylinders", "horsepower", "name"]])
print(
    df.loc[
        # * 조건
        (df["cylinders"] == 4) & (df["horsepower"] >= 100),
        # * 나타낼 열
        ["cylinders", "horsepower", "name"],
    ]
)

#      cylinders  horsepower              name
# 23           4       113.0          bmw 2002
# 76           4       112.0   volvo 145e (sw)
# 120          4       112.0       volvo 144ea
# 122          4       110.0         saab 99le
# 180          4       115.0         saab 99le
# 207          4       102.0         volvo 245
# 242          4       110.0          bmw 320i
# 271          4       105.0  plymouth sapporo
# 276          4       115.0        saab 99gle
# 323          4       105.0        dodge colt
# 357          4       100.0      datsun 200sx


#! 필터링 - isin()

# ? name이 "ford maverick" "ford mustang ii" "chevrolet impala"
filter_bool3 = (
    (df["name"] == "ford maverick")
    | (df["name"] == "ford mustang ii")
    | (df["name"] == "chevrolet impala")
)

print(df.loc[filter_bool3,])
#       mpg  cylinders  displacement  horsepower  weight  acceleration  model_year origin              name
# 6    14.0          8         454.0       220.0    4354           9.0          70    usa  chevrolet impala
# 17   21.0          6         200.0        85.0    2587          16.0          70    usa     ford maverick
# 38   14.0          8         350.0       165.0    4209          12.0          71    usa  chevrolet impala
# 62   13.0          8         350.0       165.0    4274          12.0          72    usa  chevrolet impala
# 100  18.0          6         250.0        88.0    3021          16.5          73    usa     ford maverick
# 103  11.0          8         400.0       150.0    4997          14.0          73    usa  chevrolet impala
# 126  21.0          6         200.0         NaN    2875          17.0          74    usa     ford maverick
# 155  15.0          6         250.0        72.0    3158          19.5          75    usa     ford maverick
# 166  13.0          8         302.0       129.0    3169          12.0          75    usa   ford mustang ii
# 193  24.0          6         200.0        81.0    3012          17.6          76    usa     ford maverick


# ? isin() method
filter_isin = df["name"].isin(["ford maverick", "ford mustang ii", "chevrolet impala"])

print(df.loc[filter_isin,])
#       mpg  cylinders  displacement  horsepower  weight  acceleration  model_year origin              name
# 6    14.0          8         454.0       220.0    4354           9.0          70    usa  chevrolet impala
# 17   21.0          6         200.0        85.0    2587          16.0          70    usa     ford maverick
# 38   14.0          8         350.0       165.0    4209          12.0          71    usa  chevrolet impala
# 62   13.0          8         350.0       165.0    4274          12.0          72    usa  chevrolet impala
# 100  18.0          6         250.0        88.0    3021          16.5          73    usa     ford maverick
# 103  11.0          8         400.0       150.0    4997          14.0          73    usa  chevrolet impala
# 126  21.0          6         200.0         NaN    2875          17.0          74    usa     ford maverick
# 155  15.0          6         250.0        72.0    3158          19.5          75    usa     ford maverick
# 166  13.0          8         302.0       129.0    3169          12.0          75    usa   ford mustang ii
# 193  24.0          6         200.0        81.0    3012          17.6          76    usa     ford maverick

# ? 값을 horsepower 순으로 정렬
print(df.loc[filter_isin,].sort_values("horsepower"))
