# @Time : 2020/2/4 18:11
# @Author : tongyue

from flask import Flask,render_template,url_for,redirect
from flask_login import LoginManager
login_manager = LoginManager() #创建login_manager ，保存cookie，需要在场景中导入flask_login的 login_user


# from app.web1.book import web1 改成如下

def create_app():
    app = Flask(__name__)
    print("1111111111111"+__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    return app