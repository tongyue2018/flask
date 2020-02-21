# @Time : 2020/2/21 16:41
# @Author : tongyue


class BookViewModel:

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

    @classmethod
    def package_collection(cls,data,keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = len(data['books'])
            returned['books'] = [cls._cut_book_data(book) for book in data['books']]

    @classmethod
    def _cut_book_data(cls,data):
        book = {
            'title':data['title'],
            'publisher':'、'.join(data['publisher']),
            'pages':data['pages'],
            'price':data['price'],
            'summary':data['summary'],
            'image':data['image'],
            'author':data['author']
        }
        return book
