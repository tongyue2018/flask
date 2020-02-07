# @Time : 2020/2/7 16:08
# @Author : tongyue


# sqlalchemy 第三方包，下面的Book模型映射到数据表
# flask封装了sqlalchemy，Flask_ALchemy更加人性化
# 安装lask_ALchemy：  pip install flask-sqlalchemy

# WTFORMS也是第三方工具包 flask封装了WTFORMS，Flask_WTFORMS

from sqlalchemy import Column,Integer,String

class Book(): # book 模型和操作方法
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    author = Column(String(30),nullable=True)
    isbn = ''
    price = 0
    binding = '' #平装 or 精装

    def sample(self):
        pass


