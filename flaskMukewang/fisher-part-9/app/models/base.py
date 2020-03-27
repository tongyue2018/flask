# @Time : 2020/3/12 上午9:29 
# @Author : tongyue

from sqlalchemy.orm import relationship
from app.models.base import db
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base():
    create_time = Column('create_time',Integer)
    status = Column(SmallInteger)