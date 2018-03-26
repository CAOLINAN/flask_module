# coding=utf-8
# @File  : blog.py
# @Author: PuJi
# @Date  : 3/22/18

from config import DevConfig
from flask import Flask


app = Flask(__name__)

app.config.from_object(DevConfig)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'


@app.route('/sign_in')
def register():
    return "this is token and address"


@app.route('/sign_up')
def login():
    return "this is token and token"


@app.route('/password/reset')
def reset_password():
    return "this is a new token"


@app.route('/wallet/new')
def produce_address():
    return "this is a new address"


@app.route('/source/publish')
def produce_source():
    return 'this is claim_id'


@app.route('/source/delete')
def delete_source():
    if True:
        return "True"
    else:
        return "False"


@app.route('/source/change')
def change_source():
    if True:
        return "True"
    else:
        return "False"


@app.route('/source/list')
def list_source():
    return 'This is source list'


@app.route('/source/single')
def get_source():
    return "This is a source info"


@app.route('/transaction')
def transaction():
    if True:
        return "True"
    else:
        return "False"


@app.route('/source/download')
def download_source():
    return "this is the source"


@app.route('/wallet/recharge')
def recharge_wallet():
    if True:
        return "True"
    else:
        return "False"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)