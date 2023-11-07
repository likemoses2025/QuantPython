import seaborn as sns

#! 결측치 대체하기
df = sns.load_dataset("titanic")

print(df)
print(df.head(6))  # 6줄 출력

mean_age = df["age"].mean()

print("Mean Age", mean_age)  # Mean Age 29.69911764705882

df["age"].fillna(mean_age, inplace=True)  # NaN  평균값 입력

print(df.head(6))

print(df["embark_town"])

df["embark_town"].fillna("Southampton", inplace=True)  # * inplace=True 원본 객체 변경!

#! 결측치를 직전 온전한 값으로 바꾸기
df["deck_ffill"] = df["deck"].fillna(method="ffill")
df["deck_bfill"] = df["deck"].fillna(method="bfill")

print("결측치의 값을 바로 전의 온전한 값으로 대체", df["deck", "deck_ffill", "deck_bfill"].head(12))
# * ffill : 위의 행 중 올바른 값 입력
# * pfill : 아래 행 중 올바른 값 입력
