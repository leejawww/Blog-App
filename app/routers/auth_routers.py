from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict
from fastapi import APIRouter, Body
from app.models.auth_models import UserSchema, UserLoginSchema
import jwt
import time
from decouple import config

auth_router = APIRouter(tags=["AUTH"])
Data_file = "/Users/lijahbabugongal/blog_app/app/database/auth_data.json"

SECRET = str(config("JWT_SECRET"))
ALGORITHM = str(config("JWT_ALGORITHM"))


def token_response(token: str):
    return {"access_token": token}


def signJWT(user_id: str) -> Dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + 600}
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM).decode("utf-8")
    return token_response(token)


def decodeJWT(token: str) -> Dict:
    try:
        decode_token = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return dict(decode_token) if decode_token["expires"] >= time.time() else {}
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return {}


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        credentials: HTTPAuthorizationCredentials | None = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials is None:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
        if credentials.scheme != "Bearer":
            raise HTTPException(
                status_code=403, detail="Invalid authentication scheme."
            )
        if not self.verify_jwt(credentials.credentials):
            raise HTTPException(
                status_code=403, detail="Invalid token or expired token."
            )
        return credentials

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            payload = {}
        if payload:
            isTokenValid = True
        return isTokenValid


users = []


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@auth_router.post("/user/signup")
def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)


@auth_router.post("/user/login")
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {"error": "Wrong login details!"}
