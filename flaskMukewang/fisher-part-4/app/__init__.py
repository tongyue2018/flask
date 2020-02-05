# @Time : 2020/2/4 18:11
# @Author : tongyue

from flask import Flask
# from app.web.book import web 改成如下
from app.web import web


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../../config/config.py')
    register_blueprint(app)
    return app

def register_blueprint(app):
    app.register_blueprint(web)

