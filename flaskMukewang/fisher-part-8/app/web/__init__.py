# @Time : 2020/2/4 18:13
# @Author : tongyue


from flask import Blueprint

# 蓝图机制 blueprint
web = Blueprint('web1', __name__)


from app.web import book
# from app.web1 import user
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
