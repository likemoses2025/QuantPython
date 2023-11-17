import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rc("font", family="Malgun Gothic")

# 가져올 수 있는 샘플 데이터셋 확인하기
dataset_names = sns.get_dataset_names()
print(dataset_names)

# 다이아몬드 샘플데이터 가져오기
df = sns.load_dataset("diamonds")
print(df.head())
