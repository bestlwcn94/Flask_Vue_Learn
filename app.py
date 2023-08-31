from flask import Flask, request, escape, jsonify, make_response
import os
import json
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
import datetime
app = Flask(__name__)
app.config['debug'] = True
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def hello_world1():  # put application's code here
    return 'Hello World1111111!'


@app.route('/z', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    os.system("notepad.exe")
    print(request.data)
    print(request.json.get('name'))
    print(request.json.get('password'))

    if (request.json.get('name') == '123') & (request.json.get('password') == '123'):
        return make_response(jsonify({'code': 200, 'msg': '登录成功'}), 200)
    else:
        return '登陆失败'


@app.route('/w', methods=['GET', 'POST'])
def hello_world2():  # put application's code here

    print(request.form)
    print(request.form['name'])
    print(request.form['password'])

    if (request.form['name'] == '123') & (request.form['password'] == '123'):
        return make_response(jsonify({'code': 200, 'msg': '登录成功'}), 200)
    else:
        return '登陆失败'





if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5003)
