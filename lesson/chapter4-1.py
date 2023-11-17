import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#! 한번에 여러개의 그래프 그리기
plt.rc("font", family="Malgun Gothic")
df = sns.load_dataset("penguins")

fig, axes = plt.subplots(2, 1, figsize=(10, 6))

# 첫번째 그림
axes[0].scatter(df["flipper_length_mm"], df["body_mass_g"])
axes[0].set_xlabel("날개 길이[mm]")
axes[0].set_ylabel("몸무게(g)")
axes[0].set_title("날개와 몸무게 간의 관계")

# 두번째 그림
axes[1].hist(df["body_mass_g"], bins=30)
axes[1].set_xlabel("Body Mass")
axes[1].set_ylabel("Count")
axes[1].set_title("팽귄의 몸무게 분포")

# 간격조절
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.95, wspace=0.5, hspace=0.5)
plt.show()


# ? 다른방법 첫번째 그림
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.scatter(df["flipper_length_mm"], df["body_mass_g"])
plt.xlabel("날개 길이 mm")
plt.ylabel("몸무게(g)")
plt.title("날개와 몸무게 간의 관계")

# 다른방법 두번째 그림
plt.subplot(2, 1, 2)
plt.hist(df["body_mass_g"], bins=30)
plt.xlabel("Body Mass")
plt.ylabel("Count")
plt.title("펭귄의 몸무게 분포")
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.95, wspace=0.5, hspace=0.5)
plt.show()
