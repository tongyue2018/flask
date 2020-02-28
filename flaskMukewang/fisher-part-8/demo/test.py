class BookViewModel:
    def __init__(self,book):
        self.title = book['title']
        self.publisher = book['publisher']
class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self,keyword,yushu_book):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book)  for book in yushu_book.books]
class YushuBook:
    def __init__(self):
        self.total = 100
        self.books = [
            {
                'title':'daniu',
                'publisher':['publisher1','publisher2']
            },
            {
                'title': 'daniu1',
                'publisher': ['publisher3', 'publisher4']
            }
        ]

yushu_book = YushuBook()
bookCollection = BookCollection()
bookCollection.fill('孔子',yushu_book)
print(bookCollection.books[0].title)
