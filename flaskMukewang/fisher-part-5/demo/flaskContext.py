# @Time : 2020/2/15 17:01
# @Author : tongyue


from flask import Flask,current_app,request

app = Flask(__name__)

'''
1.应用上下文机制（本质是对象） -- 对Flask的封装  -- ctx.py（源码） -- AppContext类

2.请求上下文机制（本质是对象） -- 对Request的封装  -- ctx.py（源码） -- RequextContext类

3.查看a = current_app 源码其实是个flask定义德一个代理类型LocalProxy

4.查看全局源码： External - Libararies - python - site-packages

* Flask--配置信息 路由等等
* AppContext--对Flask封装 并有额外的方法pop push等 入栈 出栈
* Request -- 保存一些请求信息
* RequextContext -- 对Request进行封装， 并有额外的方法pop push 入栈 出栈

'''
a = current_app
b = current_app.config['DEBUG']


