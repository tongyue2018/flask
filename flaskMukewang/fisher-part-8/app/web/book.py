import json

from flask import jsonify, request, render_template, flash
from app.lbs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel
from app.view_models.book import BookCollection
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

# http://127.0.0.1:5000/book/search
@web.route('/book/search')
def search():

    # 至少1个字符，有长度限制。 q = request.args['q']
    # 至少1个字符，正整数。 page = request.args['page']

    '''
    验证层,from app.forms.book import SearchForm
    验证代码如下
    '''

    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip() # 取值并去掉空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushubook = YuShuBook()

        if isbn_or_key == 'isbn':
            yushubook.search_by_isbn(q)
        else:
            yushubook.search_by_key(q,page)

        books.fill(q,yushubook)
        '''
        return jsonify(books.__dict__)
        不能直接序列化books对象 bookCollection下面的self.books是由其他对象赋值
        如果bookCollection的属性都是普通的字符 数字，则可以对books.__dict__进行序列化
        
        '''

        #对象序列化，需要传入1个函数，把所有涉及的对象转化成dict
        # return json.dumps(books,default=lambda o: o.__dict__)
    else:
        '''
        form异常返回
        '''
        # return form.errors
        # return jsonify({"msg":"参数错误"})

        '''
        消息闪现
        '''
        flash('关键字不符合要求，请重新输入')
    #form传入模板，可以再base中些，其他模板可以继承
    return render_template('search_result.html', books = books,form=form)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass


# 引入模板html
@web.route('/test')
def test():
    dictData = {
        'name':'tongyue',
        'age':18,
        'content':None
    }
    dictData1 = {

    }
    flash('hello,qiyue')
    flash('hello,tongyue')

    # render_template用来填充html模板 /app/templates/test.html
    # http://127.0.0.1:5000/test
    return render_template('test.html',data = dictData,data1 = dictData1)

'''
引入模板html,sub继承了layout.html
'''

@web.route('/sub')
def sub():
    dictData = {
        'name':'tongyue',
        'age':18
    }

    dictData1 = {

    }

    # render_template用来填充html模板 /app/templates/sub.html
    # http://127.0.0.1:5000/sub
    return render_template('sub.html',data = dictData,data1 = dictData1)
