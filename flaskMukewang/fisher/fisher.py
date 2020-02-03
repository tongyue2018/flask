
#根据isbn搜索
#根据书籍名称搜索

# API地址
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# http://t.yushu.im/v2/book/isbn/{isbn}
# https://api.douban.com/v2/book

from flask import Flask,make_response
from fisher.helper import is_isbn_or_key
from fisher.yushu_book import YuShuBook
import json

app = Flask(__name__)
app.config.from_pyfile('../../config.py')

@app.route('/book/search/<q>/<page>') # 9787501524044
def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    abc = q
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_key(q)
    headers = {
        'Content-Type': 'application/json'
    }
    # 视图函数一定要返回字符串， 所以dict要序列化
    response = make_response(json.dumps(result))
    response.headers = headers


if(__name__ == '__main__'):
    app.run(app.config['HOST'],5000,debug=True)
