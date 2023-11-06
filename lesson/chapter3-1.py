import pandas as pd

#!  데이터 불러오기 및 저장하기
data_csv = pd.read_csv(
    "https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv"
)
print(data_csv)
