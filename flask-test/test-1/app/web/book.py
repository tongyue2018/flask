import json

from flask import render_template,redirect,url_for
from app.web import web

# @web.route进行注册
# Request接收 “?”传参
'''
1、大部分框架在管理http请求都有Request Response对象
2、request几乎包含了全部的http请求信息，比如
    a、获取的查询参数
    b、post请求传递的相关参数
    c、获取电脑的ip地址，remote ip
3、调试模式可以看出，request.args[]是一个不可变字典,为dict子类 ，可以转化成可变字典，如下:
    dictArgs = request.args.to_dict()
4、requset在flask试图函数，上下文接收http请求的时候才有我们的预期对象，否则单机版则可能不是我们的预期对象。
    如：单单定义1个单机版函数 引用request，request可能是一个本地代理。
'''

# http://127.0.0.1:5000/book/search
# http://127.0.0.1:5000/static/flask_logo.jpg
@web.route('/book/search/<name>')
def search(name):
    return render_template('auth/plan1.html',name=name)

@web.route('/book/search2')
def search2():
    return (url_for('main.search',name="bcd"))  # 返回/book/search/bcd

@web.route('/book/search3/')
def search3():
    return (url_for('main.search2',name="abc")) #返回 /book/search2?name=abc