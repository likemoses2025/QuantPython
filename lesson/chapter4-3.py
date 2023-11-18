import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
print(df.head())
#    survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
# 0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
# 1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
# 2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
# 3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
# 4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True

# @ 나이와 운임과의 관계
sns.scatterplot(data=df, x="age", y="fare")
plt.show()

# @ 나이 운임 점 그래프에서 점을 class의 종류에 따라 다른 아이콘으로 표현 - hue 그룹별 색 ,  style 그룹별 모양
sns.scatterplot(data=df, x="age", y="fare", hue="class", style="class")
plt.show()

# @ 성별에 따른 생존율 - 인덱스는 class
df_pivot = df.pivot_table(
    index="class", columns="sex", values="survived", aggfunc="mean"
)
print(df_pivot)
# sex       female      male
# class
# First   0.968085  0.368852
# Second  0.921053  0.157407
# Third   0.500000  0.135447
# @ 히트맵 - annot : 데이터의 값 표현 , cmap : 파렛트 종류, coolwarm 은 높을수록 붉은색
sns.heatmap(df_pivot, annot=True, cmap="coolwarm")
plt.show()


# @ 한 번에 여러 개의 그래프 나타내기
# ? figure-level 클래스별 나이 분포
sns.displot(data=df, x="age", hue="class", kind="hist", alpha=0.3)
plt.show()


# @ class 별로 개별 그래프 그리기 - col값을 통해 각 그래프가 분리된다
sns.displot(data=df, x="age", col="class", kind="hist")
plt.show()


# @ class별 sex별 나이 그래프를 hist로 표현
sns.displot(data=df, x="age", col="class", row="sex", kind="hist")
plt.show()


#! axes-level로 그래프를 표현하는 방법
g, axes = plt.subplots(2, 1, figsize=(8, 6))
sns.histplot(data=df, x="age", hue="class", ax=axes[0])
sns.barplot(data=df, x="class", y="age", ax=axes[1])

axes[0].set_title("클래스별 나이 분포도")
axes[1].set_title("클래스별 평균 나이")

g.tight_layout()  # 여백이 조정됨
plt.show()
