from flask import Flask, request, escape, jsonify, make_response
import os
import json
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
import datetime
app = Flask(__name__)
app.config['debug'] = True
CORS(app)
app.config['JWT_SECRET_KEY'] = 'secretkey'

jwt = JWTManager(app)

# 用户信息
users = {
  '123': '456',
  'aaa': 'bbb',
}

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




@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # 验证用户名密码
    if not username or not password:

        return jsonify({"msg": "Missing username or password"}), 401

    if username not in users or users[username] != password:
        return jsonify({"msg": "Bad credentials"}), 403

    # 生成token
    access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(hours=24))

    return jsonify(access_token=access_token), 200


# 受保护接口
@app.route('/profile')
def profile():
    # 获取token
    auth_header = request.headers.get('Authorization')
    token = auth_header.split(" ")[1] if auth_header else None

    # 验证token
    if not token:
        print(666)
        return jsonify({"msg": "Missing token"}), 401

    try:
        data = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=["HS256"])
        current_user = data['sub']
    except:
        return jsonify({"msg": "Invalid token"}), 403

        # 返回用户信息
    if current_user == 'john':
        return jsonify({"profile": "John's profile"})
    elif current_user == 'mary':
        return jsonify({"profile": "Mary's profile"})

    return jsonify({"msg": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5003)
