# This File is Responsible for signing,Encoding,Decoding and returning JWTs.
import time
# import jwt
import jwt

from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

# Function returns the generated Tokens (JWTs)
def token_response(token: str):
    return {
        "access token" : token
    }


# Function used for signing the JWt string
def signJWT(userID : str):
    payload = {
        "userID" : userID,
        "expiry" : time.time() + 600 
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token : str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm = JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}