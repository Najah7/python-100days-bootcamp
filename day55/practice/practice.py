from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# NOTE: how to user decorators with parameters 👇
    # NOTE default type is string (型を指定しない場合)
@app.route('/username/<string:name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


# NOTE: デコレータを使ったHTMLのレスポンス
#   簡易的なメッセージを表示する場合などに便利。
# 　認証機能などを関数ビューで実装する場合にも便利。

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route('/hello')
@make_bold
@make_emphasis
@make_underlined
def hello():
    return "Hello, World!"

# テンプレートのレンダリング

@app.route('/hello_template')
def hello_with_template():
    return render_template('hello.html')

if __name__ == '__main__':
    # NOTE: debug=True will auto-reload the server when you make changes to the code
        # NOTE: 標準エラーのDebugger PINを使うことで、エラーの状態でのコンソールを使える（）
        app.run(debug=True)