from hashlib import algorithms_available
import jwt, datetime
from dateutil.relativedelta import relativedelta
from rest_framework import exceptions
from rest_framework.exceptions import AuthenticationFailed

# access_token 생성
def create_access_token(id):
    return jwt.encode({
        'id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        'iat': datetime.datetime.utcnow()
    },  'access_secret', algorithm ='HS256')

# access_token에서 유효기간 복호화
def access_token_exp(token):
    payload = jwt.decode(token, 'access_secret', algorithms ='HS256')
    return payload['exp']
    
# access_token에서 id 복호화
def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms ='HS256')
        return payload['id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')

# refresh_token 생성
def create_refresh_token(id):
    return jwt.encode({
        'id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    },  'refresh_secret', algorithm='HS256')

# refresh_token에서 id 복호화
def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')
        return payload['id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')