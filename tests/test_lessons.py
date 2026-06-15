# tests/test_basics.py
# 03_functions/lesson_03.py の関数をテストします

import sys
import os

# プロジェクトのルートディレクトリをパスに追加してインポートできるようにする
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from 03_functions.lesson_03 import greet, get_stats

def test_greet():
    # 挨拶関数のテスト
    assert greet("田中") == "田中さん、こんにちは！"
    assert greet("佐藤", "お疲れ様です") == "佐藤さん、お疲れ様です！"

def test_get_stats():
    # 統計計算関数のテスト
    nums = [10, 20, 30]
    total, average = get_stats(nums)
    assert total == 60
    assert average == 20.0

def test_get_stats_empty():
    # 空のリストの場合（エラーのハンドリングなどを考えるきっかけに）
    # 現状のlesson_03.pyは0除算でエラーになるはずですが、
    # テストを書くことで「こういう時どうする？」という設計の議論ができます。
    pass
