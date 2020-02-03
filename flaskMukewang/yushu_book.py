

from fisher.httpRequest import HttpRequest
class YuShuBook:

    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        result = HttpRequest.get(url)
        return result
    def search_by_key(self,keyWord,count=15,start=0):
        url = self.keyword_url.format(keyWord,count,start)
        result = HttpRequest.get(url)
        return result

