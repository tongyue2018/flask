
from flask import jsonify,request
from app.lbs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.viewModels.book import BookViewModel

from app.web import web

# @web.route进行注册
# Request接收 “?”传参
'''
1、大部分框架在管理http请求都有Request Response对象
2、request几乎包含了全部的http请求信息，比如
    a、获取的查询参数
    b、post请求传递的相关参数
    c、获取电脑的ip地址，remote ip
3、调试模式可以看出，request.args[]是一个不可变字典,为dict子类 ，可以转化成可变字典，如下:
    dictArgs = request.args.to_dict()
4、requset在flask试图函数，上下文接收http请求的时候才有我们的预期对象，否则单机版则可能不是我们的预期对象。
    如：单单定义1个单机版函数 引用request，request可能是一个本地代理。
'''
@web.route('/book/search')
def search():

    # 至少1个字符，有长度限制。 q = request.args['q']
    # 至少1个字符，正整数。 page = request.args['page']

    '''
    验证层,from app.forms.book import SearchForm
    验证代码如下
    '''

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip() # 取值并去掉空格
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        yushubook = YuShuBook()
        if isbn_or_key == 'isbn':
            result = yushubook.search_by_isbn(q)
            result = Book
        else:
            result = yushubook.search_by_key(q,page)
        return jsonify(result)
    else:
        '''
        form异常返回
        '''
        return form.errors
        # return jsonify({"msg":"参数错误"})

