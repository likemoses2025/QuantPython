import pandas as pd

#! merge() 함수 - inner join, left join , right join , outer join

df1 = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)

df2 = pd.DataFrame(
    {
        "key": ["K0", "K1", "K3", "K4"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
# ? inner join - 교집합 리턴
result1 = pd.merge(df1, df2, on="key")
result2 = pd.merge(df2, df1, on="key")
print(result1)
print(result2)
#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K3  A3  B3  C2  D2

#   key   C   D   A   B
# 0  K0  C0  D0  A0  B0
# 1  K1  C1  D1  A1  B1
# 2  K3  C2  D2  A3  B3

# ? left join - 윈쪽 프레임은 유지 되고 오른쪽 프레임이 키를 기준으로 합쳐짐
result3 = pd.merge(df1, df2, on="key", how="left")
print(result3)
#   key   A   B    C    D
# 0  K0  A0  B0   C0   D0
# 1  K1  A1  B1   C1   D1
# 2  K2  A2  B2  NaN  NaN
# 3  K3  A3  B3   C2   D2

# ? right join - 오른쪽 프레임은 유지 되고 왼쪽 프레임이 키를 기준으로 합쳐짐
result4 = pd.merge(df1, df2, on="key", how="right")
print(result4)
#   key    A    B   C   D
# 0  K0   A0   B0  C0  D0
# 1  K1   A1   B1  C1  D1
# 2  K3   A3   B3  C2  D2
# 3  K4  NaN  NaN  C3  D3

# ? outer join - 한쪽만 속하더라도 상관없이 합집합 부분을 리턴
result5 = pd.merge(df1, df2, on="key", how="outer")
print(result5)
#   key    A    B    C    D
# 0  K0   A0   B0   C0   D0
# 1  K1   A1   B1   C1   D1
# 2  K2   A2   B2  NaN  NaN
# 3  K3   A3   B3   C2   D2
# 4  K4  NaN  NaN   C3   D3

left2 = pd.DataFrame(
    {
        "key_left": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
right2 = pd.DataFrame(
    {
        "key_right": ["K0", "K1", "K3", "K4"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

# ? left join 키가 다른 경우
result6 = pd.merge(left2, right2, left_on="key_left", right_on="key_right", how="inner")
print(result6)
#   key_left   A   B key_right   C   D
# 0       K0  A0  B0        K0  C0  D0
# 1       K1  A1  B1        K1  C1  D1
# 2       K3  A3  B3        K3  C2  D2

# ? 더욱 직관적인 표현 inner는 교집합
result7 = left2.merge(right2, left_on="key_left", right_on="key_right", how="inner")
print(result7)
#   key_left   A   B key_right   C   D
# 0       K0  A0  B0        K0  C0  D0
# 1       K1  A1  B1        K1  C1  D1
# 2       K3  A3  B3        K3  C2  D2


import pandas as pd

#! join 함수 - 행 기준으로 데이터를 결합
left = pd.DataFrame(
    {
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    },
    index=["K0", "K1", "K2", "K3"],
)
right = pd.DataFrame(
    {
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    },
    index=["K0", "K1", "K3", "K4"],
)

result = left.join(right)
print(result)
