from flask import Flask
import logging

app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def register():
    app.logger.info('123')
    return 'hello world'

if(__name__ == '__main__'):
    handler = logging.FileHandler('flask.log')
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host=app.config['HOST'],port=5000,debug=True)

