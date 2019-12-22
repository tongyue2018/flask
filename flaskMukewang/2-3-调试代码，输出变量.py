from flask import Flask
import logging
logging.basicConfig(
    level=logging.DEBUG,#控制台打印的日志级别
    filename='flask.log',  # 将日志写入log_new.log文件中
    filemode='a',##模式，a追加，w覆盖
    # format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'#完整日志格式
    format='%(asctime)s - %(levelname)s: %(message)s'#日志格式
)

app = Flask(__name__)
app.config.from_pyfile('../config.py')


@app.route('/')
def register():
    app.logger.info('输出配置文件HOST常量的值:%s,时间:%s'%(app.config['HOST']))
    return 'hello world'

if(__name__ == '__main__'):
    app.run(host=app.config['HOST'],port=5000,debug=True)

# 第一步：加入logging.basicConfig基础配置。
# 第二步：输出log, app.logger.info