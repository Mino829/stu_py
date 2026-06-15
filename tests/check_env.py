# tests/check_env.py
# 学習に必要なライブラリがインストールされているか確認するスクリプト

import importlib

def check_library(lib_name):
    try:
        lib = importlib.import_name(lib_name)
        version = getattr(lib, "__version__", "unknown")
        print(f"✅ {lib_name} is installed. (version: {version})")
        return True
    except ImportError:
        print(f"❌ {lib_name} is NOT installed.")
        return False

print("--- Environment Check ---")
libraries = ["numpy", "pandas", "matplotlib", "sklearn"]
results = [check_library(lib) for lib in libraries]

if all(results):
    print("\n🎉 All required libraries are ready for Machine Learning!")
else:
    print("\n⚠️ Some libraries are missing. Please run: pip install numpy pandas matplotlib scikit-learn")
