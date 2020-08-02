# @Time : 2020/2/7 16:08
# @Author : tongyue


# sqlalchemy 第三方包，下面的Book模型映射到数据表
# flask封装了sqlalchemy，Flask_ALchemy更加人性化
# 安装lask_ALchemy：  pip install flask-sqlalchemy

# WTFORMS也是第方工具包 flask封装了WTFORMS，Flask_WTFORMS
from sqlalchemy import Column,Integer,String
#映射到数据库导入 flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
'''
注意：
1.基础的Column,Integer,String是从sqlalchemy中导入的
2.映射到数据库SQLAlchemy,是从flask_sqlalchemy中导入的
3.sqlalchemy支持多数据库  分布式数据库
'''

db = SQLAlchemy()

'''
MVC里面的M ：除了建表，还有很多操作逻辑，更多业务逻辑在model
ORM：数据库操作
'''

'''模型类 需要继承db.Model'''
class Book(db.Model):
    id = Column(Integer,primary_key=True,autoincrement=True) #自增长 主key
    title = Column(String(50),nullable=False) #是否可空
    author = Column(String(30),nullable=True)
    binding = Column(String(20)) #平装 or 精装
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15),nullable=False,unique=True)#唯一约束
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass


