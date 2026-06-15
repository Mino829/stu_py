# 04_data_libraries/lesson_04.py
# データ分析ライブラリ (NumPy, Pandas, Matplotlib)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NumPy: 数値計算（行列）
# 機械学習のデータは行列として扱われます
arr = np.array([1, 2, 3, 4, 5])
print(f"NumPy配列: {arr}")
print(f"平均: {arr.mean()}")

# 2. Pandas: データフレーム（表形式）
data = {
    'Size': [50, 60, 70, 80, 90],
    'Price': [500, 650, 700, 850, 1000]
}
df = pd.DataFrame(data)
print("Pandasデータフレーム:")
print(df.head())
print(f"Priceの統計情報:\n{df['Price'].describe()}")

# 3. Matplotlib: 可視化
plt.figure(figsize=(6, 4))
plt.scatter(df['Size'], df['Price'], color='blue', label='Actual Data')
plt.xlabel('Size (m2)')
plt.ylabel('Price (10k Yen)')
plt.title('House Size vs Price')
plt.legend()
plt.grid(True)
# plt.show()  # 実行環境に合わせてコメントアウトを外してください
print("グラフのプロット設定が完了しました。")
