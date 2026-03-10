from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # 這會去 templates 資料夾找 index.html
    return "<h1>架站成功了！</h1><p>這是你的第一個網站。</p>"

if __name__ == '__main__':
    # 啟動伺服器，debug=True 會在你改程式時自動重啟
    app.run(debug=True)