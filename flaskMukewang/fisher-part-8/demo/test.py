
class BookViewModel:
    def __init__(self,**book):
        self.title = book['title'],
        self.publisher = book['publisher']

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self,keyword,yushu_book):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(**book)  for book in yushu_book.books]


