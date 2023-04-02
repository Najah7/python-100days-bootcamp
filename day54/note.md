# フルスタックとは
フルスタック = フロントエンド + バックエンド

# pythonのフレームワークについて
- Django
- Flask

# 3層構造Webアプリケーション
- クライアント
- サーバ
- データベース
※レストランに例えていた、クライアントは客席、サーバはキッチン、データベースはレストランの食品庫

# CLIを使う利点
- 作業によっては、GUIよりもCLIの方が早い
- 作業によっては、GUIよりもCLIの方が簡単
※このほかにもCLIのことを色々と説明していた。

Remember, wiht great power comes great responsibility.（-fオプションなど使うときに思い出して（笑））

# PythonでのCLIの作成方法
__name__ == "__main__"を使う。
__main__: モジュールが直接実行されたときに、そのモジュールの名前が__main__になる。（他の場合はモジュール名になる。）

# [特殊変数について](https://docs.python.org/3/library/stdtypes.html?highlight=#special-attributes)

# デコレータ関数（Flaskでよく使うので説明している）
- 冗長性を排除するための方法の1つ。（一部の処理以外共通点が多いなどに使える）
- outter関数（関数の入れ子を）を簡潔にわかりやすい形にしたもの
- クロージャで使わることが多いと思う。（innerの関数を中で呼び出してもいいが基本的には外に返すパターンがいいと思う。）

# デコレータの使い方
```python
# 定義
def decorator(func):
    def inner(*args, **kwargs):
        # 何かの処理
        return func(*args, **kwargs)
    return inner

# 使用
@decorator
def func():
    pass
```

※多分、複数の関数でもできそう。けど、複雑性が増しそうなので、使う機会はないと思うので深堀しない。