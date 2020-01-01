
import sys
from flask import make_response
from flask_cors import CORS, cross_origin


# sys.path.append('E:\\pythonProject\\python_study\\python初学\\初学(2)')
sys.path.append('./') #效果和上面绝对路径一致

from flask import Flask, request
import json
app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
cors = CORS(app, resources={r"*": {"origins": "*"}})##方法一：全局配置跨域

@app.route("/")
def start():
    return json.dumps({
        'code': '00',
        'msg': 'ok'
    })

@app.route("/regist", methods=["GET", "POST","OPTIONS"])
# @cross_origin()##方法二：局部配置跨域
def regist():
    username = "form表单 get请求---"+str(request.form.get('username'))
    passwd = "form表单 get请求---"+str(request.form.get('passwd'))
    if(request.form.get('username') == None or request.form.get('passwd') == None) : #判断get post 2种方式，第一种如上/login，第二种如下都获取一遍
        username = "form表单 post请求---"+str(request.args.get('username'))
        passwd = "form表单 post请求---"+str(request.args.get('passwd'))
    headerName = request.headers.get('headerName') #获取header中字段值
    jsonContent = request.get_json(silent=True)  #获取json整体入参（一般放到body中），如果body中传递的是表单则获取方式还是request.form.get或者request.args.get
    dict = {
        'username': username,
        'passwd': passwd,
        'headerName':headerName,
        'jsonContent':jsonContent
    }
    jsonFormatResult = json.dumps(dict, indent=3)


    #返回header
    response = make_response(jsonFormatResult)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
