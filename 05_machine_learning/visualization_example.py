"""
簡単な可視化サンプル。依存: pandas, matplotlib
実行: python visualization_example.py
"""
import pandas as pd
import matplotlib.pyplot as plt

# サンプルデータ
data = {
    'age': [25, 30, 35, 22, 28, 40, 50, 29, 33, 38],
    'salary': [40000, 50000, 60000, 38000, 52000, 70000, 90000, 48000, 61000, 68000],
    'department': ['sales','engineering','engineering','hr','sales','engineering','management','sales','hr','engineering']
}

df = pd.DataFrame(data)

# ヒストグラム
plt.figure(figsize=(6,4))
plt.hist(df['age'], bins=5, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 散布図
plt.figure(figsize=(6,4))
plt.scatter(df['age'], df['salary'], c='green')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()

# 部署ごとの平均給料（棒グラフ）
mean_salary = df.groupby('department')['salary'].mean().reset_index()
plt.figure(figsize=(6,4))
plt.bar(mean_salary['department'], mean_salary['salary'], color='orange')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.show()

print('可視化サンプル完了')
