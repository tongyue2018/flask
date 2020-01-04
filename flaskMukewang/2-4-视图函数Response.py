from flask import Flask
import logging

app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def register():
    app.logger.info('hello')
    return 'hello world'

if(__name__ == '__main__'):
    logging.basicConfig(
        level=logging.DEBUG,  # 控制台打印的日志级别
        filename='flask.log',  # 将日志写入log_new.log文件中
        filemode='w',  ##模式，a追加，w覆盖
        # format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'#完整日志格式
        format='%(asctime)s - %(levelname)s: %(message)s'  # 日志格式
    )
    app.run(host=app.config['HOST'],port=5000,debug=True)