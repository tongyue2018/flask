import json

from flask import render_template,redirect,url_for,session,request
from app.web import web


@web.route('/book/search')
def search():
    canshu = request.args
    print(canshu['q'],type(canshu))
    print(canshu['page'], type(canshu))
    return render_template('auth/plan1.html',canshu=canshu)
