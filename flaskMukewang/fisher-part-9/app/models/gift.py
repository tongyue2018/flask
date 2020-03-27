# @Time : 2020/3/12 上午9:28 
# @Author : tongyue
from sqlalchemy.orm import relationship

from app.models.base import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Gift(db.Model):
    id =Column(Integer,primary_key = True)
    launched = Column(Boolean,default = False)
    user = relationship('User')
    # user.id  user取的上面的变量
    uid = Column(Integer,ForeignKey("user.id"))
    #因为book不是放在数据库，是通过api获取的，所以不采用下面的方式。
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey("book.id"))
    isbn = Column(String(15),nullable=False)#唯一约束需要去掉

