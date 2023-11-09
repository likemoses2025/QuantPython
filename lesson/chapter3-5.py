import pandas as pd

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
df4 = pd.DataFrame(
    {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    }
)

s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")

result = pd.concat([df1, df2, df3])
print(result)
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

# ? 행합치기
result1 = pd.concat([df1, df4])
print(result1)
#      A   B    C   D    F
# 0   A0  B0   C0  D0  NaN
# 1   A1  B1   C1  D1  NaN
# 2   A2  B2   C2  D2  NaN
# 3   A3  B3   C3  D3  NaN
# 0  NaN  B2  NaN  D2   F2
# 1  NaN  B3  NaN  D3   F3
# 2  NaN  B6  NaN  D6   F6
# 3  NaN  B7  NaN  D7   F7

# ? 열 합치기
result2 = pd.concat([df1, df4], axis=1)
print(result2)
#     A   B   C   D   B   D   F
# 0  A0  B0  C0  D0  B2  D2  F2
# 1  A1  B1  C1  D1  B3  D3  F3
# 2  A2  B2  C2  D2  B6  D6  F6
# 3  A3  B3  C3  D3  B7  D7  F7

# ? 교집합 합치기
result3 = pd.concat([df1, df4], axis=1, join="inner")
print(result3)
#     A   B   C   D   B   D   F
# 0  A0  B0  C0  D0  B2  D2  F2
# 1  A1  B1  C1  D1  B3  D3  F3
# 2  A2  B2  C2  D2  B6  D6  F6
# 3  A3  B3  C3  D3  B7  D7  F7

# ? 시리즈 합치기
result4 = pd.concat([df1, s1], axis=1)
print(result4)
