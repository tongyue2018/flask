# @Time : 2020/2/20 10:42
# @Author : tongyue


from flask import Flask


app = Flask(__name__)


@app.route('/')
def login():
    return 'ABC'

if(__name__ == '__main__'):
    app.run(host='0.0.0.0',port='5000',debug=True,threaded=True)

'''
app.run，开启多线程模式 <==> 单核，多线程

'''
