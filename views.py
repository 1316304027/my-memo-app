from flask import render_template
from app import app

#======================================================================================  #▲▲▲▲▲ リスト7.3追加 ▲▲▲▲▲
# ルーティング 路由选择
#======================================================================================  <!-- ▼▼▼▼▼ flashメッセージ ▼▼▼▼▼ -->

# モジュールのインポート
from werkzeug.exceptions import NotFound

#エラーハンドリング
@app.errorhandler(404)
def show_404_page(error):
    msg=error.description
    print('エラー内容：',msg)
    return render_template('errors/404.html',msg=msg), 404

