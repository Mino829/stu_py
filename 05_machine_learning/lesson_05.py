# 05_machine_learning/lesson_05.py
# 機械学習入門 (Scikit-learn)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. データの読み込み (アヤメのデータセット)
iris = load_iris()
X = iris.data  # 特徴量 (がくの長さ、幅など)
y = iris.target # ラベル (品種: 0, 1, 2)

# 2. データを学習用とテスト用に分割
# 80%を学習に、20%をテストに使用します
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. モデルの選択と学習 (K-近傍法)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 4. 予測と評価
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"予測結果: {y_pred}")
print(f"正解率: {accuracy * 100:.2f}%")

# 5. 未知のデータで予測
new_data = [[5.1, 3.5, 1.4, 0.2]] # 1つのサンプルのデータ
prediction = model.predict(new_data)
print(f"未知のデータの予測品種: {iris.target_names[prediction][0]}")
