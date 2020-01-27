from flask import Flask
import logging

app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def register():
    app.logger.info('输出配置文件HOST常量的值:%s'%(app.config['HOST']))
    return 'hello world'

if(__name__ == '__main__'):
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        filename='log_new.log',  # 将日志写入log_new.log文件中
                        filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                        # 日志格式
                        )

    # handler = logging.FileHandler('flask123.log', encoding='UTF-8')
    # handler.setLevel(logging.DEBUG)
    # logging_format = logging.Formatter(
    #     '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    # handler.setFormatter(logging_format)
    # app.logger.addHandler(handler)
    # app.run(host=app.config['HOST'],port=5000,debug=True)

# 第一步：加入logging.basicConfig基础配置。
# 第二步：输出log, app.logger.info