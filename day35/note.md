# Environment Variableの特徴
- ## key&valueの形式
- ## すべて文字列

# Environment Variableの利点
- ## Environment Variableを変えるだけで挙動変えるなどの使い方ができる。
- ## コードに機密情報を載せずに済む点（セキュリティ的に良い）

# 設定方法
```bash
export KEY=VALUE
```

# 確認方法
```bash
env
```

# pythonでの使い方
```python
import os

os.environ.get('<key name>')
```