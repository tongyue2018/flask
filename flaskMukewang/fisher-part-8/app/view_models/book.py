# @Time : 2020/2/21 16:41
# @Author : tongyue


'''
面向对象
1.需要有描述特征（类变量，实例变量）
2.需要有行为（方法等）
'''

class BookViewModel:
    def __init__(self,**book):
        self.title = book['title'],
        self.publisher = book['publisher'],
        self.pages = book['pages'],
        self.price = book['price'],
        self.summary = book['summary'],
        self.image = book.get('image'),
        self.author = book['author']

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self,keyword,yushu_book):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(**book)  for book in yushu_book.books]


#此处为反实例，并不是面向对象思想
class _BookViewModel:

    @classmethod
    def package_single(cls,data,keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returned['total'] = 1
        returned['books'] = [cls._cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls,data,keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls._cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def _cut_book_data(cls,data):
        book = {
            'title':data['title'],
            'publisher':'、'.join(data['publisher']),
            'pages':data['pages'] or '',#处理null情况 如果data['pages']为null则返回''，data['pages']不为null则返回data['pages']
            'price':data['price'],
            'summary':data['summary']  or '',
            'image':data['image'],
            'author':data['author']
        }
        return book
'''
处理null 变成''，可以用如下操作data['pages'] or ''，如果data['pages']为null则返回''，data['pages']不为null则返回data['pages']
'''
