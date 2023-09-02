from api.authentication.utils import validate_token,generate_token
from flask import Blueprint, request, jsonify
auth_bp = Blueprint('user', __name__)

from flask import Blueprint, request, jsonify


users = {
    '123': '456',
    'mary': '5678'
}


@auth_bp.route('/login', methods=['POST','OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        # 返回响应头部信息
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, headers
    if request.method == 'POST':

        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return jsonify({'error': 'Missing credentials'}), 400

        if username not in users or users[username] != password:
            return jsonify({'error': 'Invalid credentials'}), 401
        if users[username] == password:
            access_token = generate_token(username)
            return jsonify({'msg': 'Login successful!','Authorization':access_token}), 200


@auth_bp.route('/profile',methods=['GET','OPTIONS'])
def profile():
    if request.method == 'OPTIONS':
        # 返回响应头部信息
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 200, headers
    if request.method =='GET':
    # 获取token
        print("profile",request.headers)
        auth_header = request.headers.get('Authorization')
        print(auth_header)
        token = auth_header.split(" ")[0] if auth_header else None

        # 验证token
        if not token:
            print(666)
            return jsonify({"msg": "Missing token"}), 401

        try:
            data = validate_token(token)
            print(data)
            current_user = data['user']
            print(current_user,"data['user']",type(current_user))
        except:
            return jsonify({"msg": "Invalid token"}), 403

            # 返回用户信息
        if current_user == '123':
            return jsonify({"profile": current_user})
        elif current_user == 'mary':
            return jsonify({"profile": "Mary's profile"})
        else:
            return jsonify({"msg": "User not found"}), 404