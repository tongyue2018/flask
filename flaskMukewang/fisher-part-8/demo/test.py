# @Time : 2020/2/26 10:55
# @Author : tongyue


class BookViewModel:
    def __init__(self,**book):
        print(book['title'])

dictData = {
    "title":"123"
}
a = BookViewModel(**dictData)

