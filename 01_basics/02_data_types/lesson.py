# 02_data_types/lesson.py
# レッスン2: データの種類 (型)

# Pythonには、データの種類がいくつかあります。
# 種類が違うと、できることが変わります。

# 1. 整数 (int)
apple_count = 5

# 2. 小数 (float)
price = 198.5

# 3. 文字列 (str)
shop_name = "Pythonフルーツ店"

# 4. 真偽値 (bool)
# 正しい(True)か、間違っている(False)かの2つの値だけです。
is_open = True

# 型を調べる方法 (type関数)
print(type(apple_count)) # <class 'int'> と表示されます
print(type(shop_name))   # <class 'str'> と表示されます

# 型が違うと足し算ができない場合があります
# print(apple_count + shop_name) # これはエラーになります！
