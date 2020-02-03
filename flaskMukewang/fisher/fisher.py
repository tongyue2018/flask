
#根据isbn搜索
#根据书籍名称搜索

# API地址
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# http://t.yushu.im/v2/book/isbn/{isbn}
# https://api.douban.com/v2/book

# http://127.0.0.1/book/search/9787501524044

from flask import Flask,make_response
from helper import  is_isbn_or_key
from yushu_book import YuShuBook
import json

app = Flask(__name__)
app.config.from_pyfile('../../config.py')

@app.route('/book/search/<q>/<page>') #
def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    yushubook = YuShuBook()
    if isbn_or_key == 'isbn':
        result = yushubook.search_by_isbn(q)
    else:
        result = yushubook.search_by_key(q)
    headers = {
        'Content-Type': 'application/json'
    }
    # 视图函数一定要返回字符串， 所以dict要序列化
    response = make_response(json.dumps(result))
    response.headers = headers
    return response


if(__name__ == '__main__'):
    app.run(app.config['HOST'],5000,debug=True)
