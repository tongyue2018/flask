
from httpRequest import HttpRequest
from app.setting import PER_PAGE

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    def search_by_isbn(self,isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HttpRequest.getBookInfo(url)
        return result

    def search_by_key(self,keyWord,page=1):
        url = self.keyword_url.format(keyWord, self.calculate_start(page, PER_PAGE), PER_PAGE)
        result = HttpRequest.getBookInfo(url)
        return result

    def calculate_start(self, page, PER_PAGE):
        return (page - 1) * PER_PAGE

'''
1.区分配置文件,PER_PAGE从配置文件setting.py中读取
2.(page-1)*PER_PAGE抽离出函数currentPage
'''
