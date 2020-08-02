# @Time : 2020/3/28 8:56 
# @Author : tongyue
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models.user import User

class RegisterForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message="电子邮箱不符合规范")])
    password = PasswordField(validators=[DataRequired(message="密码不能为空，请输入您的密码"),Length(6,32)])
    nickname = StringField(validators=[DataRequired(),Length(2,10,message="昵称至少2个字符，最多10个字符")])

    #自定义验证器，处理业务逻辑相关的验证，必须以validate开头

    def validate_email(self,field): # _email表示对上面的email做校验
        # db.session 可以查询
        # 更快捷的查询
        if User.query.filter_by(email=field.data).first(): #first最多只返回一条
            raise ValidationError("电子邮箱已经被注册")
class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(8,64),Email(message="电子邮箱不符合规范")])
    password = PasswordField(validators=[DataRequired(message="密码不能为空，请输入您的密码"),Length(6,32)])