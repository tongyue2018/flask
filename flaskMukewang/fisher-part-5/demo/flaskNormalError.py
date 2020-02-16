# @Time : 2020/2/15 17:01
# @Author : tongyue


from flask import Flask,current_app,request

app = Flask(__name__)

a = current_app
b = current_app.config['DEBUG']



'''
见上下文学习 flaskContext.py

RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
to interface with the current application object in some way. To solve
this, set up an application context with app.app_context().  See the
documentation for more information.


'''
