# coding=utf-8
# @File  : blog.py
# @Author: PuJi
# @Date  : 3/22/18

from config import DevConfig
from flask import Flask, redirect
from flask import render_template
from flask import Markup
from flask import abort

app = Flask(__name__)

app.config.from_object(DevConfig)


@app.route('/')
def home():
    return '<h1>Hello World!</h1>'



if __name__ == '__main__':
    app.run()