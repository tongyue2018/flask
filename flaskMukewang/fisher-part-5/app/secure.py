# @Time : 2020/2/7 10:34
# @Author : tongyue


DEBUG = True

'''

pymyql or cymql驱动需要pip安装
fisher为database名称

'''


#pymyql
SQLALCHEMY_DATABASE_URI= "mysql+pymysql://%s:%s@%s:%s/fisher" %("root","Qwe123!!!","47.107.58.164","3306")

#cymysql SQLALCHEMY_DATABASE_URI='mysql+cymyql://root:Qwe123!!!@47.107.58.164:3306/fisher'



