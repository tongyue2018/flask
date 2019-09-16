
from flask import Flask,request
import json
app = Flask(__name__)

@app.route("/")
def start():
  return json.dumps({
    'code': '00',
    'msg':'ok'
  })

@app.route("/login",methods=["GET","POST"])
def login():
  if request.method == "POST":
      username = request.form.get('username')
      passwd = request.form.get('passwd')
  else: # 以GET方式传参数，通过args取值
      username = request.args.get('username')
      passwd = request.args.get('passwd')
  
  print(username,passwd)

  dict = {
      'username':username,
      'passwd':passwd
  }
  return json.dumps(dict)

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0', port=5000)
