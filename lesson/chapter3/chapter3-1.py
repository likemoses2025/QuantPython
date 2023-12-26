import pandas as pd

#!  데이터 불러오기 및 저장하기
data_csv = pd.read_csv(
    "https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv"
)
print(data_csv)

# ? csv로 저장하기 data_csv.to_csv("data.csv") #!

data_excel = pd.read_excel(
    "https://github.com/hyunyulhenry/quant_py/raw/main/kospi.xlsx", sheet_name="kospi"
)

print(data_excel)
# ? excel로 저장하기 data_excel.to_excel("exceldata.xlsx")


#! 데이터 요약 정보 및 통계값 살펴보기

import seaborn as sns

df = sns.load_dataset("titanic")
# * df.to_excel("titanic.xlsx") =>엑셀 파일로 추출하기
print(df.head())  # * 앞부분 5줄
print(df.tail())  # * 끝부분 5줄

print("데이터 프레임의 크기", df.shape)  # * 891 , 15 => 행15 열 891
print("데이터 프레임의 정보", df.info)  # * 891 , 15 => 행15 열 891

print("성별 숫자 : ", df["sex"].value_counts())
print("나이별 숫자 : ", df["age"].value_counts())

print("성별 생존/사망 숫자 : ", df[["sex", "survived"]].value_counts())

print(
    "성별 생존/사망 점유비 : ", df[["sex", "survived"]].value_counts(normalize=True).sort_index()
)

print("평균값 : 생존율과 같다", df["survived"].mean())
print("생존율 , 평균나이", df[["survived", "age"]].mean())

print("탑승비용 최소값", df["fare"].min())
print("탑승비용 최대값", df["fare"].max())
print("탑승비용 평균값", df["fare"].mean())
print("탑승비용 중위수", df["fare"].median())


#! 결측치(NaN - Not a Number , 누락값) 처리하기
# * info method를 통해 결측치가 아닌 데이터의 개수를 확인
print("결측치가 아닌 값 정보", df.info())

# ? 결측치를 찾는 메소드
# * isnull() : 결측치면 True or False
# * notnull() :유효 데이터면 True or False

print(df.head().isnull())

# ? 결측치 삭제하기
print("결측치 삭제", df.dropna())  # * 결측치가 있으면 해당 행을 모두 삭제

print("age 행방향 결측치만 삭제", df.dropna(subset=["age"], axis=0))

print("열방향 결측치 삭제", df.dropna(axis=1))

print("결측치가 300개 이상인 열만 삭제", df.dropna(axis=1, thresh=300))
