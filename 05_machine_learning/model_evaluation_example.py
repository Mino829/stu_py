"""
モデル評価の簡単な例。依存: scikit-learn, pandas
実行: python model_evaluation_example.py
"""
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             confusion_matrix, roc_auc_score, roc_curve)
import numpy as np

# 合成データ
X, y = make_classification(n_samples=200, n_features=5, n_informative=3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# モデル学習
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
probs = clf.predict_proba(X_test)[:, 1]
preds = (probs >= 0.5).astype(int)

# 指標計算
acc = accuracy_score(y_test, preds)
prec = precision_score(y_test, preds)
rec = recall_score(y_test, preds)
f1 = f1_score(y_test, preds)
cm = confusion_matrix(y_test, preds)
auc = roc_auc_score(y_test, probs)

print('Accuracy:', acc)
print('Precision:', prec)
print('Recall:', rec)
print('F1:', f1)
print('Confusion Matrix:\n', cm)
print('ROC AUC:', auc)

# 閾値を変えて適合率／再現率を観察
thresholds = np.linspace(0.1, 0.9, 9)
print('\nThreshold analysis:')
for t in thresholds:
    p = (probs >= t).astype(int)
    print(f't={t:.2f} -> precision={precision_score(y_test,p):.3f}, recall={recall_score(y_test,p):.3f}')

# ROC 曲線の例データ（出力は配列）
fpr, tpr, _ = roc_curve(y_test, probs)
print('\nROC curve points (first 5):')
for i in range(min(5, len(fpr))):
    print(f'fpr={fpr[i]:.3f}, tpr={tpr[i]:.3f}')

print('\nモデル評価サンプル完了')
