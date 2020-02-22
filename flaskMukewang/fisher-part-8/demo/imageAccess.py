# @Time : 2020/2/22 14:36
# @Author : tongyue

'''


1.默认静态文件位置--根目录--app-static
app = Flask(__name__)，__name__指向app目录static文件夹

http://127.0.0.1:5000/static/flask_logo.jpg

2.更改静态资源文件目录-1
app = Flask(__name__,static_folder='view_models/statics')

http://127.0.0.1:5000/statics/flask_logo.jpg



3.更改静态资源文件目录-2,如果存在static_url_path，则按照static_url_path，自己研究
app = Flask(__name__,static_folder='view_models/statics'，static_url_path=)


'''
