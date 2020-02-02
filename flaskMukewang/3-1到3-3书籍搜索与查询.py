
#根据isbn搜索
#根据书籍名称搜索

# API地址
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# http://t.yushu.im/v2/book/isbn/{isbn}
# https://api.douban.com/v2/book

from flask import Flask,make_response

app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def register():
    response = make_response('<h1>hello world</h1>')
    headers = {
        'content-type':'text/plain' #说明不区分大小写
    }
    response.headers = headers
    app.logger.info(response)
    return response


if(__name__ == '__main__'):
    app.run(app.config['HOST'],5000,debug=True)

