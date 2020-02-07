# 根据isbn搜索
# 根据书籍名称搜索

# API地址
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# http://t.yushu.im/v2/book/isbn/{isbn}
# https://api.douban.com/v2/book
# http://127.0.0.1:5000/book/search/9787501524044/1


# 入口文件只做初始化和启动工作，视图函数根据拆分到对应单独文件中，一个项目可以有多个视图函数。
from flask import Flask, jsonify
from .helper import is_isbn_or_key
from .yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_pyfile('../config/config.py')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    yushubook = YuShuBook()
    if isbn_or_key == 'isbn':
        result = yushubook.search_by_isbn(q)
    else:
        result = yushubook.search_by_key(q, 0, page)

    # headers = {
    #     'Content-Type': 'application/json'
    # }
    #
    # # 视图函数一定要返回字符串， 所以dict要序列化
    # response = make_response(json.dumps(result))
    # response.headers = headers
    # return response

    # 采用jsonfy,等同于如上操作
    return jsonify(result)


if (__name__ == '__main__'):
    app.run(app.config['HOST'], 5000, debug=True)
