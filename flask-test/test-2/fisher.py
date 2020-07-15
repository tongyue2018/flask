# 根据isbn搜索
# 根据书籍名称搜索

# API地址
# http://127.0.0.1:5000/book/search2

from flask import Flask,render_template,url_for,redirect
#可以从包中导入其中__init__.py的方法、变量
from app import create_app

# app的初始化可以放到__init__文件中，导包方式如：from app import create_app
app = create_app()

@app.route('/book/search')
def search():
    return render_template('auth/plan1.html')

@app.route('/book/search2')
def search2():
    return redirect(url_for('search'))

if (__name__ == '__main__'):
    app.run(app.config['HOST'], 5000, debug=True,threaded=True)
'''
读取config区分文件配置，secure.py,setting.py
'''
