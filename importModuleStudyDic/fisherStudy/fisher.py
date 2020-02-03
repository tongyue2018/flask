
#根据isbn搜索
#根据书籍名称搜索

# API地址
# http://t.yushu.im/v2/book/search?q={}&start={}&count={}
# http://t.yushu.im/v2/book/isbn/{isbn}
# https://api.douban.com/v2/book

# http://127.0.0.1/book/search/9787501524044M

import sys
sys.path.append('E:\python_study\pythonStart\import-module')
print(sys.path)

from importModuleStudyDic.fisherStudy.helper import  is_isbn_or_key
from yushu_book import YuShuBook


def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    yushu = YuShuBook()
    if isbn_or_key == 'isbn':
        result = yushu.search_by_isbn(q)
    else:
        result = yushu.search_by_key(q)
    return result

print(search('9787501524044',10))
