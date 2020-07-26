# @Time : 2020/2/7 16:08
# @Author : tongyue


# sqlalchemy 第三方包，下面的Book模型映射到数据表
# flask封装了sqlalchemy，Flask_ALchemy更加人性化
# 安装lask_ALchemy：  pip install flask-sqlalchemy

# WTFORMS也是第三方工具包 flask封装了WTFORMS，Flask_WTFORMS
from sqlalchemy import Column,Integer,String,Boolean,Float
#映射到数据库导入 flask_sqlalchemy
from werkzeug.security import generate_password_hash,check_password_hash

from app.models.base import db, Base
from flask_login import UserMixin
from app import login_manager
'''
注意：
1.基础的Column,Integer,.tring是从sqlalchemy中导入的
2.映射到数据库SQLAlchemy,是从flask_sqlalchemy中导入的
3.sqlalchemy支持多数据库  分布式数据库
'''

'''
MVC里面的M ：除了建表，还有很多操作逻辑，更多业务逻辑在model
ORM：数据库操作
'''

'''模型类 需要继承db.Model'''

class User(Base, UserMixin):
    # __tablename__='user1' 可以指定表名，否则取class后面的User
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(50))
    _password = Column('password', String(128), nullable=False)  # 对应数据库名字 password

    # 以下2个是属性预处理  自动处理
    @property
    def password(self):
        return self._password

    @password.setter #属性装饰器 password.setter的password为属性名称
    def password(self,raw): #raw是password属性传入的值
        self._password = generate_password_hash(raw)

    def check_password(self,passw):
        return check_password_hash(self._password,passw) #passw是明文密码，函数会将它加密再和数据库密码做比较

    #flask-login login_user将信息存入cookie，以模型中的get_id为标准写入对应的数据
    def get_id(self):
        return self.id

#获取用户的模型， 访问权限用到，视图函数中加入@login_required ，它需要这个函数
@login_manager.user_loader  #login_manager是app中自己初始化的
def get_user(uid):
    User.query.get(int(uid))