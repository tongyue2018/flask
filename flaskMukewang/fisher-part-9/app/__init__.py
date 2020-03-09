# @Time : 2020/2/4 18:11
# @Author : tongyue

from flask import Flask
# from app.web.book import web 改成如下
from app.web import web

from app.models.book import db

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

    '''
    1. db与核心对象app关联 db.init_app(app)
    2. 数据库配置固定名称SQLALCHEMY_DATABASE_URI，无序调用app.config.from_object('app.secure')即可，SQLALCHEMY_DATABASE_URI='mysql+pymyql://root:Qwe123!!!@47.107.58.164:3306/fisher'
    3. db.create_all()将所有模型（models文件夹下的模型）映射到数据库
    secure.py中加入数据库配置即可
    '''

    db.init_app(app)
    db.create_all(app=app)  #看源码已贴在最下方 第1种：传入app  第2种：存在current_app，则把上下文推入当前栈即可，代码如下 with app.app_context(): 第3中db = SQLAlchemy(app=app)初始化的时候传入app
    # with app.app_context():
    #     db.create_all()

    return app

    '''
    b.create_all(app=app)  不加app=app则会报错， 见demo文件夹中上下文context学习
    c.
    '''

def register_blueprint(app):
    app.register_blueprint(web)



'''
    def get_app(self, reference_app=None):
        """Helper method that implements the logic to look up an
        application."""

        if reference_app is not None:
            return reference_app

        if current_app:
            return current_app._get_current_object()

        if self.app is not None:
            return self.app

'''
