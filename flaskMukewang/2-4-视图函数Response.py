from flask import Flask,make_response

app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def register():
    app.logger.info('hello')
    # response = make_response('<h1>hello</h1>') #默认返回html
    # response.headers['Content-type'] = 'text/plain' #返回普通字符

    response = make_response('<h1>hello world</h1>')
    # response = make_response('<h1>hello world</h1>',301) #返回码301时重定向到location的地址

    response.statusCode = 200
    headers = {
        'location':'https://www.baidu.com',
        'Content-Type':'text/html'
        # 'Content-Type':'text/plain'

    }
    response.headers = headers
    app.logger.info(response)
    return response

if(__name__ == '__main__'):
    app.run(host=app.config['HOST'],port=5000,debug=True)
#
# 一、视图函数默认status code:200
# 可返回301和 location:"重定向地址"
#
# 二、视图函数默认header，第一个html
# Content-Type:text/html
# Content-Type:application/json
# Content-Type:text/plain --普通字符
# Content-Type:application/x-www-form-urlencoded -- 一般requests请求form表单接口时候用到。
