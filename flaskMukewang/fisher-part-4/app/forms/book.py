# @Time : 2020/2/6 15:47
# @Author : tongyue


from wtforms import Form,StringField,IntegerField
from wtforms.validators import Length,NumberRange

def SearchForm(Form):
    q = StringField(validators=[Length(min=1,max=30)])
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)
'''

可以给默认值default

'''
