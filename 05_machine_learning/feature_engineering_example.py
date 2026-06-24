"""
特徴量エンジニアリングの簡単な例。依存: pandas, numpy, scikit-learn
実行: python feature_engineering_example.py
"""
import pandas as pd
import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 合成データ（回帰）
X, y = make_regression(n_samples=200, n_features=5, n_informative=3, noise=10, random_state=1)
cols = [f'f{i}' for i in range(X.shape[1])]
df = pd.DataFrame(X, columns=cols)
df['target'] = y

# 単純な新特徴量
df['f0_times_f1'] = df['f0'] * df['f1']
df['f0_plus_f2'] = df['f0'] + df['f2']

# 多項式特徴量
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_feats = poly.fit_transform(df[cols])
poly_cols = poly.get_feature_names_out(cols)
poly_df = pd.DataFrame(poly_feats, columns=poly_cols)

# 結合してデータセットを作る
full_df = pd.concat([df.drop(columns=cols), poly_df], axis=1)
X_full = full_df.drop(columns=['target']).values
y_full = full_df['target'].values

# 訓練/検証分割
X_train, X_test, y_train, y_test = train_test_split(X_full, y_full, test_size=0.3, random_state=42)

# 特徴量選択（統計的手法）
selector = SelectKBest(score_func=f_regression, k=8)
selector.fit(X_train, y_train)
X_train_sel = selector.transform(X_train)
X_test_sel = selector.transform(X_test)
selected_idx = selector.get_support(indices=True)
print('SelectKBest selected feature indices:', selected_idx)

# ランダムフォレストで重要度を算出
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)
importances = rf.feature_importances_
# 上位8を表示
top_idx = np.argsort(importances)[-8:][::-1]
print('RandomForest top feature indices (by importance):', top_idx)

# モデル比較: 全特徴量 vs 選択後
rf_all = RandomForestRegressor(random_state=42)
rf_all.fit(X_train, y_train)
pred_all = rf_all.predict(X_test)
mse_all = mean_squared_error(y_test, pred_all)

rf_sel = RandomForestRegressor(random_state=42)
rf_sel.fit(X_train_sel, y_train)
pred_sel = rf_sel.predict(X_test_sel)
mse_sel = mean_squared_error(y_test, pred_sel)

print(f'MSE (all features): {mse_all:.3f}')
print(f'MSE (selected features): {mse_sel:.3f}')

print('\nfeature_engineering_example 完了')
