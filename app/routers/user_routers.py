from fastapi import APIRouter, HTTPException, Depends
from app.models.user_models import User
from app.schemas.user_schemas import UserCreate
from app.database.database import get_db
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


@user_router.post("/user/create", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.model_dump())
    # if id == new_user.id:
    #     raise HTTPException(status_code=400, detail="User id already exist.")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@user_router.get("/user/view/{id}")
def view_user(id: int):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="User not found.")
    id = id - 1
    return data[id]


@user_router.delete("/user/remove/{id}")
def remove_user(id: int):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="User not found.")
    data.pop(id - 1)
    save_data(data)
    return "User removed successfully"
