from flask import Flask
import sys

app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def register():
    return 'hello world'

if(__name__ == '__main__'):
    app.run(host=app.config['HOST'],port=5000,debug=True)

# 先了解第一种，from_pyfile
# 读取app.config是1个字典，从py文件中读取的值。
