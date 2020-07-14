import requests
from flask import render_template, request, redirect, url_for, flash
from app.models.base import  db
from app.web import web

__author__ = '七月'

from app.forms.auth import RegisterForm, LoginForm
from app.models.user import User
from flask_login import login_user


@web.route('/register', methods=['GET', 'POST'])  # 默认只支持get，register.html表单提交的post，所以这边接收也是post
def register():
    form = RegisterForm(request.form) #注意这里不一样，教程里面的是form 提取表单提交的参数，book里面的额是request.args提取get方法
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        #user模型写入数据库  orm思想操作数据库
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web1.login')) #一定要return才能结束掉这个试图函数
    return render_template('auth/register.html',form=form); #form包含了错误信息和输入信息，输入错误以后可以提示，还可以保存用户输入的信息


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user,remember=True) #True表示存入的Cookie是持续性的cookie 默认365天，不写则是一次性的
            next = request.args.get("next")
            if  not next or not next.startwith('/'):
                next = url_for('web1.index')
            return redirect(next)  #一定要return才能结束掉这个试图函数

            # flask-login login_user将信息存入cookie，以模型中的get_id为标准写入对应的数据，user模型中定义函数如下：
            # def get_id(self):
            #     return self.id
            # from flask_login import UserMixin  user需要继承UserMixin的各种方法，继承以后则不需要get_id，前提是模型中唯一标识也是id这个字段
            # class User(Base, UserMixin):

            # login_manager = LoginManager()  # 创建login_manager ，保存cookie需要在场景中导入flask_login的 login_user

            # 初始化的时候要加三段代码
            # login_manager = LoginManager()  # 创建login_manager ，保存cookie需要在场景中导入flask_login的 login_user
            # @login_manager.user_loader
            # def load_user(user_id):
            #     user = db.session.query(User).get(user_id)
            #     return user
            #
            # def create_app():
            #     app = Flask(__name__)
            #     register_blueprint(app)
            #     login_manager.init_app(app)  # 初始化login_manager

        else:
            flash("账号不存在或者密码错误")
    return render_template('auth/login.html',form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
