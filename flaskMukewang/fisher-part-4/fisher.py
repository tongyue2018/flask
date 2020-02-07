# 根据isbn搜索
# 根据书籍名称搜索

# API地址
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# http://t.yushu.im/v2/book/isbn/{isbn}
# https://api.douban.com/v2/book
# http://127.0.0.1:5000/book/search/9787501524044/1


# 入口文件只做初始化和启动工作，视图函数根据拆分到对应单独文件中，一个项目可以有多个视图函数。

#可以从包中导入其中__init__.py的方法、变量
from app import create_app
from app.setting import HOST

# app的初始化可以放到__init__文件中，导包方式如：from app import create_app
app = create_app()

if (__name__ == '__main__'):
    app.run(HOST, 5000, debug=True)
'''
读取config区分文件配置，secure.py,setting.py
'''
