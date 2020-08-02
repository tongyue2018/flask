from . import web


__author__ = '七月'


@web.route('/')
def index():
    return "welcom to flask"


@web.route('/personal')
def personal_center():
    pass
