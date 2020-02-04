
from flask import jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook


# 蓝图机制 blueprint

@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    yushubook = YuShuBook()
    if isbn_or_key == 'isbn':
        result = yushubook.search_by_isbn(q)
    else:
        result = yushubook.search_by_key(q, 0, page)
    return jsonify(result)
