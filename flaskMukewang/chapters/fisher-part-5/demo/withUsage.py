# @Time : 2020/2/15 17:01
# @Author : tongyue


from flask import Flask,current_app,request

app = Flask(__name__)


# ctx = app.app_context()
# ctx.push()
# a = current_app
# b = current_app.config['DEBUG']
# ctx.pop()

'''
上面代码简写，app.app_context()对象实现了如下方法，可以用with ,平时代码设计中也可以这么设计， 比如文件读写释放资源不需要f.close  数据库链接释放资源

    def __enter__(self):
        self.push()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.pop(exc_value)
'''
with app.app_context():
    a = current_app #离开了with 其实已经ctx.pop() ，current_app不会有值了
    b= current_app.config['DEBUG']

