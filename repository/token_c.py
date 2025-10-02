import datetime
import jwt
from jwt.exceptions import InvalidTokenError
from models import schemas


Secrect_key = "dec601be5976230de6b4c5621278ebce78c867cd2752c0dd6d78e39a4a04a1e4"
Algorithm = "HS256"
ACCESS_TOKEN_EXPIRES_MINUTES = 30

def create_access_token(data: dict, expires_delta: datetime.timedelta| None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.now(datetime.timezone.utc)+ expires_delta 
    else:
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Secrect_key, algorithm=Algorithm)
    return encoded_jwt

def verificar_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, Secrect_key, algorithms=[Algorithm])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    
