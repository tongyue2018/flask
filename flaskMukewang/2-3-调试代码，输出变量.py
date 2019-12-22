from flask import Flask
import sys

app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def register():
    return 'hello world'

if(__name__ == '__main__'):
    app.run(host=app.config['HOST'],port=5000,debug=1)
    app.logger.debug('1232')
    app.logger.warning('123')
    app.logger.error('123')
    app.logger.info('123')
