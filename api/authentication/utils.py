from datetime import datetime

import jwt


# 生成JWT
def generate_token(user):
    payload = {
        'sub': user,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return token


# 验证JWT
def validate_token(token):
    try:
        payload = jwt.decode(token, 'secret', algorithm='HS256')
        return payload['sub']
    except:
        return False
