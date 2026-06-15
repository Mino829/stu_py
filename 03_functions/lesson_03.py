# 03_functions/lesson_03.py
# 関数とモジュール

# 1. 関数の定義
def greet(name, message="こんにちは"):
    """挨拶を返す関数"""
    return f"{name}さん、{message}！"

# 関数の呼び出し
print(greet("田中"))
print(greet("佐藤", "お疲れ様です"))

# 2. 複数の戻り値 (タプルを返す)
def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, average

nums = [10, 20, 30, 40, 50]
s, avg = get_stats(nums)
print(f"合計: {s}, 平均: {avg}")

# 3. 標準ライブラリのインポート
import math
import random

print(f"円周率: {math.pi}")
print(f"ランダムな整数: {random.randint(1, 100)}")
