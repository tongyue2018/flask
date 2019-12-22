from flask import Flask

app = Flask(__name__)

#路由写为/register 此时是唯一URL，浏览器访问/register/提示404
#路由写为/register/ 此时浏览器访问/register 视图函数返回status code：301或308，location：/register，可以通过浏览器调试工具查看效果
@app.route('/register/')
def register():
    return 'hello world'

if(__name__ == '__main__'):
    app.run(debug=True,host='0.0.0.0',port=5000)


#  http://127.0.0.1:5000/register/