from flask import Flask, request, escape, jsonify, make_response
from api.authentication.utils import  generate_token,validate_token
import os
from functools import wraps
from flask_cors import CORS
from api.authentication.user import   auth_bp
app = Flask(__name__)
app.register_blueprint(auth_bp)
app.config['debug'] = True
CORS(app)

def check_token(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        print(token)
        if not token:
            return jsonify({'error': 'Unauthorized'}), 401

        payload = validate_token(token)
        print(token,payload)
        if not payload:
            return jsonify({'error': 'Invalid token'}), 403

        user_id = payload['user']
        # current_user_id = get_current_user()
        if  not user_id :
            return jsonify({'error': 'Invalid user'}), 403

        return f(*args, **kwargs)

    return wrapper
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Headers', 'Authorization')
  return response
@app.route('/k', methods=['GET', 'POST'])
def hello_world1():  # put application's code here
    return 'Hello World1111111!'


@app.route('/z', methods=['GET', 'POST'])
@check_token
def hello_world():  # put application's code here
    # os.system("notepad.exe")
    print(request.args)
    print(request.args.get('username'))
    print(request.args.get('password'))

    if (request.args.get('username') == '123') & (request.args.get('password') == '456'):
        return make_response(jsonify({'code': 200, 'msg': '登录成功'}), 200)
    else:
        return '登陆失败'


# @app.route('/w', methods=['GET', 'POST'])
# @check_token
# def hello_world2():  # put application's code here
#
#     print(request.form)
#     print(request.form['username'])
#     print(request.form['password'])
#
#     if (request.form['username'] == '123') & (request.form['password'] == '123'):
#         return make_response(jsonify({'code': 200, 'msg': '登录成功'}), 200)
#     else:
#         return '登陆失败'





if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5003)
