# @Time : 2020/3/12 上午9:29 
# @Author : tongyue

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model): #Base继承了base.Model，所以models/book.py等模型继承Base，就是继承了base.Model

    # 我们想创建一个基类，让其他的表继承于它，但是我们又不希望基类创建成表，则在基类里面添加
    # __abstract__ = True
    __abstract__ = True

    create_time = Column('create_time',Integer)
    status = Column(SmallInteger,default=1) #0表示已删除

    #子类可以继承，用来给注册新信息赋值（用户名 密码 邮箱等等）
    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
                setattr(self,key,value)