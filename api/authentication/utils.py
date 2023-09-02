import datetime as dt

import jwt


# 生成JWT
def generate_token(user):
    payload = {
        'user': user,
        'exp': dt.datetime.utcnow() + dt.timedelta(days=1)
    }
    token = jwt.encode(payload, 'secret', 'HS256')
    print("generate_token", token,len(token))
    return token


# 验证JWT
def validate_token(token):
    try:
        print("validate_token", token,len(token))
        payload = jwt.decode(token, 'secret', 'HS256')
        return payload
    except:
        return False
