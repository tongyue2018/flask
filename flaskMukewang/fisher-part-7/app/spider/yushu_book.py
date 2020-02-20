
from app.lbs.httpRequest import HttpRequest
from flask import current_app
import json

class YuShuBook:
    '''
    模型层 MVC M层,新建一个models文件夹，存放M层所有模型
    MVC里面的M 处理建表，还有很多操作逻辑，多业务逻辑更放在M层
    '''
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    def search_by_isbn(self,isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HttpRequest.getBookInfo(url)
        return result

    def search_by_key(self,keyWord,page=1):
        url = self.keyword_url.format(keyWord, self.calculate_start(page), current_app.config['PER_PAGE'])
        result = HttpRequest.getBookInfo(url)
        return result

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']


'''
1.区分配置文件,PER_PAGE从配置文件setting.py中读取
2.(page-1)*current_app.config['PER_PAGE']抽离出函数currentPage
'''
