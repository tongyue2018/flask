# @Time : 2020/2/15 17:01
# @Author : tongyue


from flask import Flask,current_app,request

app = Flask(__name__)

a = current_app
b = current_app.config['DEBUG']


