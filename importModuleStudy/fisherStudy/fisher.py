
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

# 导包的两种方式
# 一、在同一文件夹下，直接导入文件名字即可，命令行 和 pycharm执行都没问题
# 二、如果不在同一文件夹下，需要从项目根目录开始写（不需要写项目目录名称） 如 importModuleStudyDic.fisherStudy.helper
# 方式二importModuleStudyDic.fisherStudy.helper命令行执行会报错 找不到包
# 三、命令行执行，sys.path只有当前文件执行目录 没有项目目录，因此可能需要main.py方式解决。

from importModuleStudy.fisherStudy.helper import  is_isbn_or_key
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
