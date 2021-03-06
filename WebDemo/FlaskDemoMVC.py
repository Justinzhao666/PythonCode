#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Flask通过render_template()函数来实现模板的渲染。 \
    使用模板 \
'

__author__ = 'Justin Zhao'

# if you want to change the default setting format:
# Setting -> Code Style -> File and Code Templates

from flask import Flask
from flask import request,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()