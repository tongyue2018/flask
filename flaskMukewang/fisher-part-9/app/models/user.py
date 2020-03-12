# @Time : 2020/2/7 16:08
# @Author : tongyue


# sqlalchemy 第三方包，下面的Book模型映射到数据表
# flask封装了sqlalchemy，Flask_ALchemy更加人性化
# 安装lask_ALchemy：  pip install flask-sqlalchemy

# WTFORMS也是第三方工具包 flask封装了WTFORMS，Flask_WTFORMS
from sqlalchemy import Column,Integer,String,Boolean,Float
#映射到数据库导入 flask_sqlalchemy

from app.models.base import db

'''
注意：
1.基础的Column,Integer,String是从sqlalchemy中导入的
2.映射到数据库SQLAlchemy,是从flask_sqlalchemy中导入的
3.sqlalchemy支持多数据库  分布式数据库
'''

'''
MVC里面的M ：除了建表，还有很多操作逻辑，更多业务逻辑在model
ORM：数据库操作
'''

'''模型类 需要继承db.Model'''
class User(db.Model):
    id = Column(Integer,primary_key=True)
    nickname = Column(String(24),nullable=False)
    phone_number = Column(String(18),unique=True)
    email = Column(String(50),unique=True,nullable=False)
    confirmed = Column(Boolean,default=False)
    beans = Column(Float,default=0)
    send_counter = Column(Integer,default=0)
    receive_counter = Column(Integer,default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(50))





