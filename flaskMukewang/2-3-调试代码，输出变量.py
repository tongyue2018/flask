from flask import Flask
import logging,time

# from logging.config import dictConfig
#
# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })

app = Flask(__name__)
app.config.from_pyfile('../config.py')


@app.route('/')
def register():
    timeStr = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    app.logger.debug('输出配置文件HOST常量的值:%s,时间:%s'%(app.config['HOST'],timeStr))
    return 'hello world'

if(__name__ == '__main__'):
    handler = logging.FileHandler('flask.log',encoding='utf-8')
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host=app.config['HOST'],port=5000,debug=True)