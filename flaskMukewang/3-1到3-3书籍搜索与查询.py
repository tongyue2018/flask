
#根据isbn搜索
#根据书籍名称搜索

# API地址
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# http://t.yushu.im/v2/book/isbn/{isbn}
# https://api.douban.com/v2/book

from flask import Flask,make_response
from helper import is_isbn_or_key
app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/book/search/<q>/<page>')
def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    pass

if(__name__ == '__main__'):
    app.run(app.config['HOST'],5000,debug=True)
