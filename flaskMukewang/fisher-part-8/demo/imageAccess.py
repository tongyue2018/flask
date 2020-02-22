# @Time : 2020/2/22 14:36
# @Author : tongyue

'''
静态文件属于蓝图也属于应用  html jpg 等等

1.应用默认静态文件位置--根目录/app/static
app = Flask(__name__)，__name__指向app目录static文件夹

http://127.0.0.1:5000/static/flask_logo.jpg

2.应用更改静态资源文件目录-1
app = Flask(__name__,static_folder='view_models/statics')

http://127.0.0.1:5000/statics/flask_logo.jpg



3.应用更改静态资源文件目录-2,如果存在static_url_path，则按照static_url_path，自己研究
app = Flask(__name__,static_folder='view_models/statics'，static_url_path=)


4.蓝图注册静态文件
web = Blueprint('web', __name__,static_folder='view_models/statics'，static_url_path=)

默认在 根目录/web/static


5.template_folder 指定应用模板文件夹位置，
app = Flask(__name__,template_folder=)
'''

# 目录位置：
# 应用：相对app的目录（去掉app/）
# 蓝图：相对web的目录（去掉web/）
