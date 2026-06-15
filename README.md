# Python for Machine Learning: Beginner's Path

このプロジェクトは、Pythonの基礎から機械学習の実装までをステップバイステップで学ぶための学習用ディレクトリです。

## カリキュラム構成

### 1. Pythonの基本 (`01_basics/`)
- **01_print_and_variables**: 画面出力と変数の使い方
- **02_data_types**: 数値、文字列、真偽値の違い
- **03_operators**: 算術演算と計算の優先順位
- **04_strings**: 文字列の結合や便利な埋め込み方法 (f-strings)

### 2. 制御構造とデータ構造 (`02_control_flow_and_data/`)
- 条件分岐 (if) とループ (for, while)
- リスト、辞書、タプル、集合の活用

### 3. 関数とモジュール化 (`03_functions/`)
- 関数の定義、引数、戻り値
- スコープと標準ライブラリの利用

### 4. データ分析ライブラリ (`04_data_libraries/`)
- **NumPy**: 高速な数値計算
- **Pandas**: データフレームによるデータ操作
- **Matplotlib**: データの可視化

### 5. 機械学習入門 (`05_machine_learning/`)
- Scikit-learnを用いた回帰と分類
- モデルの評価と改善

## 実行環境のセットアップ

推奨環境: Python 3.9以上

```bash
# 必要なライブラリのインストール
pip install numpy pandas matplotlib scikit-learn pytest
```

## テストの実行
自分の書いたコードが正しいか、テストツール（pytest）を使って確認できます。

```bash
# 全てのテストを実行
pytest
# 環境チェックを実行
python tests/check_env.py
```
