from flask import Flask

#実行
if __name__=='__main__':
    app.run()

#インスタンス生成
app=Flask(__name__)

#ルーティング
@app.route('/')
def hello_world():
    return '<h1>こんちゃっす</h1>'