import jwt

secret = "Secreto"

def gen_token(data):
    return jwt.encode(data, secret, algorithm="HS256")

def validate_token(token):
    try:
        return { "token" : jwt.decode(token, secret, algorithms=["HS256"])}
    except jwt.ExpiredSignatureError:
        return { "message": 'El Token ha expirado'}
    except jwt.InvalidTokenError:
        return { "message": 'El Token es invalido'}