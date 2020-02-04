
import sys
sys.path.append('./')
from httpRequest import HttpRequest
class YuShuBook:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    # @staticmethod
    def search_by_isbn(self,isbn):
        url = YuShuBook.isbn_url.format(isbn)
        result = HttpRequest.getBookInfo(url)
        return result

    @staticmethod
    def search_by_key(self,keyWord,count=15,start=0):
        url = self.keyword_url.format(keyWord,count,start)
        result = HttpRequest.getBookInfo(url)
        return result
