# 02_control_flow_and_data/lesson_02.py
# 制御構造とデータ構造

# 1. 条件分岐 (if)
score = 85
if score >= 90:
    print("評価: A")
elif score >= 70:
    print("評価: B")
else:
    print("評価: C")

# 2. リスト (List) - データの並び
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(f"フルーツリスト: {fruits}")
print(f"最初の要素: {fruits[0]}")

# 3. ループ処理 (for, while)
print("リストの中身をループ:")
for fruit in fruits:
    print(f"- {fruit}")

print("rangeを使ったループ:")
for i in range(3):
    print(f"回数: {i}")

# 4. 辞書 (Dictionary) - キーと値のペア
# 機械学習では、特徴量の名前と値の対応などでよく使います
user = {
    "name": "Alice",
    "level": 5,
    "skills": ["Python", "Math"]
}
print(f"ユーザー名: {user['name']}")
