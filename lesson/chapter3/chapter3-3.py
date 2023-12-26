import seaborn as sns

#! 인데스 다루기

df = sns.load_dataset("mpg")
print(df.head())
#     mpg  cylinders  displacement  horsepower  weight  acceleration  model_year origin                       name
# 0  18.0          8         307.0       130.0    3504          12.0          70    usa  chevrolet chevelle malibu
# 1  15.0          8         350.0       165.0    3693          11.5          70    usa          buick skylark 320
# 2  18.0          8         318.0       150.0    3436          11.0          70    usa         plymouth satellite
# 3  16.0          8         304.0       150.0    3433          12.0          70    usa              amc rebel sst
# 4  17.0          8         302.0       140.0    3449          10.5          70    usa                ford torino

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
