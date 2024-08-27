from fastapi import APIRouter, HTTPException, Depends
from app.infrastructure.models.user_models import User
from app.api.schemas.user_schemas import UserCreate
from app.core.jwt.jwt_bearer import JWTBearer

# from app.controllers.user_controller import UserControl
from app.core.database import get_db
from sqlalchemy.orm import Session
import json
import os

user_router = APIRouter(tags=["USER"])

Data_file = "/Users/lijahbabugongal/blog_app/app/database/user_data.json"


def load_data():
    if not os.path.exists(Data_file):
        with open(Data_file, "w") as f:
            json.dump({}, f)
    with open(Data_file, "r") as f:
        return json.load(f)


def save_data(data):
    with open(Data_file, "w") as f:
        json.dump(data, f, indent=4)


@user_router.post(
    "/user/create", dependencies=[Depends(JWTBearer())], response_model=UserCreate
)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.model_dump())
    # if id == new_user.id:
    #     raise HTTPException(status_code=400, detail="User id already exist.")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# def create_user(
#     user: UserCreate,
#     db: Session = Depends(get_db),
#     user_control: UserControl = Depends(),
# ):
#     return user_control.create(user)


@user_router.get(
    "/user/view/{id}", dependencies=[Depends(JWTBearer())], response_model=UserCreate
)
def view_user(id: int, db: Session = Depends(get_db)):
    results = db.query(User)
    id = id - 1
    return results[id]


@user_router.delete("/user/remove/{id}", dependencies=[Depends(JWTBearer())])
def remove_user(id: int):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="User not found.")
    data.pop(id - 1)
    save_data(data)
    return "User removed successfully"


# def remove_user(
#     id: int, user_control: UserControl = Depends(), db: Session = Depends(get_db)
# ):
#     return user_control.delete(id)
