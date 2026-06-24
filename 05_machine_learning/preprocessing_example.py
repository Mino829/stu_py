"""
簡単な前処理の例。外部ファイルに依存しないサンプルデータで動作確認ができます。
実行: python preprocessing_example.py
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler

# サンプルデータ
data = {
    'age': [25, 30, None, 22, 28],
    'salary': [50000, 60000, 55000, None, 52000],
    'department': ['sales', 'engineering', 'sales', 'hr', None]
}

df = pd.DataFrame(data)
print('元データ:\n', df, '\n')

# 1) 欠損値の確認
print('欠損値のカウント:\n', df.isna().sum(), '\n')

# 2) 欠損値処理（簡単な戦略）
df_clean = df.copy()
# 数値は中央値で埋める
df_clean['age'] = df_clean['age'].fillna(df_clean['age'].median())
df_clean['salary'] = df_clean['salary'].fillna(df_clean['salary'].median())
# カテゴリは'unknown'で埋める
df_clean['department'] = df_clean['department'].fillna('unknown')
print('欠損値処理後:\n', df_clean, '\n')

# 3) カテゴリ変換（ワンホット）
df_encoded = pd.get_dummies(df_clean, columns=['department'], drop_first=False)
print('ワンホット変換後:\n', df_encoded, '\n')

# 4) スケーリング
scaler = StandardScaler()
num_cols = ['age', 'salary']
df_encoded[num_cols] = scaler.fit_transform(df_encoded[num_cols])
print('スケーリング後:\n', df_encoded, '\n')

# 5) 保存の例（pandasのto_csv）
# df_encoded.to_csv('preprocessed_sample.csv', index=False)
print('サンプル前処理完了')
