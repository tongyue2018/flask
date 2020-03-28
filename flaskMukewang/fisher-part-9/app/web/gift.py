
from . import web
__author__ = '七月'
from flask_login import login_required


# 在user里面添加函数，获取用户的模型，并且标识@login_manager.user_loder
# @login_manager.user_loder  #login_manager是app中自己初始化的
# def get_user(uid):
#     User.query.get(int(uid))

@web.route('/my/gifts')
@login_required  #需要登录以后才能访问,要放到route的下面
def my_gifts():
    return "my gifts"


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



