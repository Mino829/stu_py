# 01_basics/lesson_01.py
# Pythonの基本: 変数、データ型、演算

# 1. 変数とデータ型
name = "Python学習者"  # 文字列型 (str)
age = 20               # 整数型 (int)
height = 170.5         # 浮動小数点型 (float)
is_beginner = True      # 布爾型 (bool)

print(f"名前: {name}, 年齢: {age}, 身長: {height}")

# 2. 基本的な演算
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")    # 割り算 (小数)
print(f"{a} // {b} = {a // b}")  # 切り捨て除算
print(f"{a} % {b} = {a % b}")    # 余り
print(f"{a} ** {b} = {a ** b}")  # べき乗

# 3. 型の変換
age_str = str(age)
print("年齢の型: " + str(type(age_str)))
