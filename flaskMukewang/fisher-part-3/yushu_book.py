
from .httpRequest import HttpRequest
class YuShuBook:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    def search_by_isbn(self,isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HttpRequest.getBookInfo(url)
        return result

    def search_by_key(self,keyWord,start=0,count=15):
        url = self.keyword_url.format(keyWord,start,count)
        result = HttpRequest.getBookInfo(url)
        return result

