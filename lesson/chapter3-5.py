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
