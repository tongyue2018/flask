# @Time : 2020/2/6 15:47
# @Author : tongyue


from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange,DataRequired

class SearchForm(Form): #（继承Form 类，可以通过request.args传递参数过来）
    q = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    page = IntegerField(validators=[DataRequired(),NumberRange(min=1,max=99,message='自定义异常-page参数传递不合法')],default=1)

'''

1. q page 可以给默认值default。

2.可以使用多个验证器，DataRequired(),Length

3. DataRequired()把 空格 空参数作为异常

4. 常信息有默认 message：，调用层web.book.py：return form.errors
{
  "q": [
    "Field must be between 1 and 30 characters long."
  ]
}


'''
