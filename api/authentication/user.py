from utils import validate_token,generate_token
from flask import Blueprint, request, jsonify
auth_bp = Blueprint('user', __name__)


from flask import Blueprint, request, jsonify


users = {
    '123': '456',
    'mary': '5678'
}


@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing credentials'}), 400

    if username not in users or users[username] != password:
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = generate_token(username)
    return jsonify({'message': 'Login successful!'}), 200


@auth_bp.route('/profile')
def profile():
    # 获取token
    auth_header = request.headers.get('Authorization')
    token = auth_header.split(" ")[1] if auth_header else None

    # 验证token
    if not token:
        print(666)
        return jsonify({"msg": "Missing token"}), 401

    try:
        data = validate_token(token)
        current_user = data['sub']
    except:
        return jsonify({"msg": "Invalid token"}), 403

        # 返回用户信息
    if current_user == 'john':
        return jsonify({"profile": "John's profile"})
    elif current_user == 'mary':
        return jsonify({"profile": "Mary's profile"})

    return jsonify({"msg": "User not found"}), 404