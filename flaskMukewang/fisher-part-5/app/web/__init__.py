# @Time : 2020/2/4 18:13
# @Author : tongyue


from flask import Blueprint

# 蓝图机制 blueprint
web = Blueprint('web1', __name__)


from app.web import book
# from app.web1 import user
