# @Time : 2020/2/15 17:01
# @Author : tongyue


from flask import Flask,current_app,request

app = Flask(__name__)

'''
1.应用上下文机制 -- 对Flask的封装

2.请求上下文机制 -- 对Request的封装

'''
a = current_app
b = current_app.config['DEBUG']


