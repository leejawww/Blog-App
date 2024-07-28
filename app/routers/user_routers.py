from fastapi import APIRouter, HTTPException
from app.schemas.user_schemas import UserCreate
import json
import os

user_router = APIRouter()

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


@user_router.post("/user/create", tags=["USER"])
def create_user(user: UserCreate):
    data = load_data()
    if any(p["id"] == user.id for p in data):
        raise HTTPException(status_code=400, detail="User id already exist.")
    data.append(user.model_dump())
    save_data(data)
    return user


@user_router.get("/user/view/{id}", tags=["USER"])
def view_user(id: int):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="User not found.")
    id = id - 1
    return data[id]


@user_router.delete("/user/remove/{id}", tags=["USER"])
def remove_user(id: int):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="User not found.")
    data.pop(id - 1)
    save_data(data)
    return "User removed successfully"
