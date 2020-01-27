
#根据isbn搜索
#根据书籍名称搜索

from flask import Flask,make_response
import logging
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
    logging.basicConfig(
        level=logging.DEBUG,  # 控制台打印的日志级别
        filename='flask.log',  # 将日志写入log_new.log文件中
        filemode='w',  ##模式，a追加，w覆盖
        # format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'#完整日志格式
        format='%(asctime)s - %(levelname)s: %(message)s'  # 日志格式
    )
    app.run(app.config['HOST'],5000,debug=True)

