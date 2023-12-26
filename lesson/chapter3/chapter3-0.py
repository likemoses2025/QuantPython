import pandas as pd

#! 시리즈란 데이터가 순차적으로 나열된 1차원 배열로 키와 값으로 구성

# ? 딕셔너리를 사용한 시리즈 작성
dict_data = {"a": 1, "b": 2, "c": 3}
series = pd.Series(dict_data)
print(series)
# a    1
# b    2
# c    3
# dtype: int64
print(type(series))  # pandas.core.series.Series
print(series.index)  # pandas.core.series.Series
print(series.values)  # pandas.core.series.Series

# ? 리스트를 통한 시리즈 만들기
list_data = ["a", "b", "c"]
series_2 = pd.Series(list_data)
print(series_2)
# 0    a
# 1    b
# 2    c
# dtype: object

series_3 = pd.Series(list_data, index=["index1", "index2", "index3"])
print(series_3)
# index1    a
# index2    b
# index3    c
# dtype: object


# ? 원소 선택하기
capital = pd.Series(
    {"Korea": "Seoul", "Japan": "Tokyo", "China": "Beijing", "India": "New Delhi"}
)
print(capital)
print(capital["Korea"])  # Seoul
print(capital[["Korea", "Japan"]])  # Seoul Tokyo
print(capital[0])  # Seoul
print(capital[1])  # Tokyo
print(capital[[0, 3]])  # type: ignore [[]] ==> 데이터프레임으로 나타남
# Korea        Seoul
# India    New Delhi
print(capital[0:3])  # Tokyo
# Korea      Seoul
# Japan      Tokyo
# China    Beijing

# ? 시리즈 연산하기
series_11 = pd.Series([1, 2, 3])
series_22 = pd.Series([4, 5, 6])

series_33 = series_11 + series_22
print(series_33)  # 5 7 9 인덱스가 같은 값끼리 더해짐
print(series_11 * 2)  # 2,4,6

# ! DataFrame 데이터 프레임 : 2차원 배열 - 엑셀의 형열표

dict_data = {"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]}
df = pd.DataFrame(dict_data)
print(df)
#    col1  col2  col3
# 0     1     4     7
# 1     2     5     8
# 2     3     6     9

df2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df2)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

df3 = pd.DataFrame(
    [
        [1, 2, 3],
        [
            4,
            5,
            6,
        ],
        [7, 8, 9],
    ],
    index=["id1", "id2", "id3"],
    columns=["col1", "col2", "col3"],
)
print(df3)
#      col1  col2  col3
# id1     1     2     3
# id2     4     5     6
# id3     7     8     9

# ? 행이름 바꾸기

df3.index = ["행1", "행2", "행3"]  # type: ignore
df3.columns = ["열1", "열2", "열3"]
print(df3)
#     열1  열2  열3
# 행1   1   2   3
# 행2   4   5   6
# 행3   7   8   9

df3.rename(index={"행1": "첫 번째 행"}, inplace=True)
df3.rename(columns={"열1": "첫 번째 열"}, inplace=True)
print(df3)
#         첫 번째 열  열2  열3
# 첫 번째 행       1   2   3
# 행2           4   5   6
# 행3           7   8   9

# ? 행,열 삭제하기
df3.drop("행3", axis=0, inplace=True)
df3.drop("열3", axis=1, inplace=True)
print(df3)

# ? 행과 열을 선택하기
dict_data2 = {
    "col1": [1, 2, 3, 4],
    "col2": [5, 6, 7, 8],
    "col3": [9, 10, 11, 12],
    "col4": [13, 14, 15, 16],
}
df = pd.DataFrame(dict_data2, index=["idx1", "idx2", "idx3", "idx4"])
print(df)
print(df["col1"])
print(df.col1)
print(df[["col1", "col2"]])  # 대괄호 2개는 데이터프레임 형태반환
#       col1  col2
# idx1     1     5
# idx2     2     6
# idx3     3     7
# idx4     4     8

print(df.loc["idx1"])  # return Series
print(df.iloc[0])  # return Series
# col1     1
# col2     5
# col3     9
# col4    13

print(df.loc[["idx1"]])  # return Data Frame
print(df.iloc[[0]])  # return Data Frame
#       col1  col2  col3  col4
# idx1     1     5     9    13

print(df.loc["idx1":"idx3"])
#       col1  col2  col3  col4
# idx1     1     5     9    13
# idx2     2     6    10    14
# idx3     3     7    11    15

print(df.iloc[0:3])  # 0,1,2
#       col1  col2  col3  col4
# idx1     1     5     9    13
# idx2     2     6    10    14
# idx3     3     7    11    15

print(df.loc["idx1", "col2"])  # 5

print(df.loc[["idx1", "idx3"], ["col1", "col4"]])
#       col1  col4
# idx1     1    13
# idx3     3    15

print(df.loc["idx1":"idx2", "col1":"col3"])
#       col1  col2  col3
# idx1     1     5     9
# idx2     2     6    10

print(df.iloc[0, 0])  # 1
print(df.iloc[[0, 2], [0, 3]])
#       col1  col4
# idx1     1    13
# idx3     3    15

print(df.iloc[0:2, 0:3])
#       col1  col2  col3
# idx1     1     5     9
# idx2     2     6    10
