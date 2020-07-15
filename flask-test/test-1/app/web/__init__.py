# @Time : 2020/2/4 18:13
# @Author : tongyue


from flask import Blueprint

# 蓝图机制 blueprint
web = Blueprint('web', __name__)

print("web初始化名称"+__name__)
from app.web import book