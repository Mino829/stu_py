# 04_strings/lesson.py
# レッスン4: 文字列を操ろう

# 1. 文字列の結合
first_name = "太郎"
last_name = "山田"
full_name = last_name + " " + first_name
print("氏名:", full_name)

# 2. 文字列の繰り返し
print("わーい！" * 3)

# 3. f-strings (エフ文字列) ★超重要
# 文字列の中に変数を埋め込む便利な方法です。
age = 25
message = f"私の名前は{full_name}です。{age}歳です。"
print(message)

# 4. 文字列の長さ
print("名前の文字数:", len(full_name))
