from fastapi import APIRouter
from app.schemas.user_schemas import UserCreate

user_routers = APIRouter()
data = []


@user_routers.post("/login", tags=["USER"])
def create_user(user: UserCreate):
    data.append(user.model_dump())
    return data


@user_routers.get("/login/{id}", tags=["USER"])
def view_user(id: int):
    id = id - 1
    return data[id]


@user_routers.delete("/login/{id}", tags=["USER"])
def delete_user(id: int):
    data.pop(id - 1)
    return data
