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
