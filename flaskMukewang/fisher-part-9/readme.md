# 欢迎进入第9章  用户登录与注册
----

> * 9-1 viewmodel意义的体现与filter函数的巧妙应用（view_models book.py）
> * 9-2 书籍详情页面业务逻辑分析
> * 9-3 实现书籍详情页面
> * 9-4 模型与模型关系
> * 9-5 自定义基类模型
> * 9-6 用户注册
> * 9-7 Python的动态赋值
> * 9-8 Python属性描述符实现getter与setter
> * 9-9 ORM的方式保存模型
> * 9-10 自定义验证器
> * 9-11 redirect重定向 
> * 9-12 cookie
> * 9-13 cookie的应用
> * 9-14 login_user 将用户信息写入cookie
> * 9-15 访问权限控制
> * 9-16 重定向攻击


1.书记详情
![](markdownImg/book-detail.png)

2.思维导图
![](markdownImg/siweidaotu.png)

3.属性的get set方法研究
 @property
    def password(self):
        return self._password

    @password.setter #属性装饰器
    def password(self,raw):
        self._password = generate_password_hash(raw)
4.hasattr和setattr研究
子类可以继承，用来给注册新信息赋值（用户名 密码 邮箱等等）
    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
                setattr(self,key,value)