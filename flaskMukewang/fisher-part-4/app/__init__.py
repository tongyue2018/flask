# @Time : 2020/2/4 18:11
# @Author : tongyue

from flask import Flask
# from app.web.book import web 改成如下
from app.web import web

def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    '''
    初始化配置文件
    统一flask的app对象管理
    其他文件不好读取app，可以from flask import current_app
    
    '''
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    return app

def register_blueprint(app):
    app.register_blueprint(web)

