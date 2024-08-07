from fastapi import APIRouter, Body  # , Depends
from app.infrastructure.models.auth_models import AuthUser
from app.core.jwt.jwt_bearer import signJWT
# from app.api.schemas.auth_schemas import AuthUserCreate
# from sqlalchemy.orm import Session
# from app.database.database import get_db

auth_router = APIRouter(tags=["AUTH"])


users = []


def check_user(data: AuthUser):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# @auth_router.post("/user/signup", response_model=AuthUserCreate)
# def create_user(user: AuthUserCreate, db: Session = Depends(get_db)):
#     new_user = AuthUser(**user.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return signJWT(new_user.email)


@auth_router.post("/user/signup")
def create_user(user: AuthUser):
    users.append(user)
    return signJWT(user.email)


@auth_router.post("/user/login")
def user_login(user: AuthUser = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {"error": "Wrong login details!"}
