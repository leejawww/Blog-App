from fastapi import APIRouter, HTTPException
from app.schemas.blog_schemas import BlogCreate
import json
import os


blog_routers = APIRouter()

Data_file = "/Users/lijahbabugongal/blog_app/app/database/blog_data.json"


def load_data():
    if not os.path.exists(Data_file):
        with open(Data_file, "w") as f:
            json.dump({}, f)
    with open(Data_file, "r") as f:
        return json.load(f)


def save_data(data):
    with open(Data_file, "w") as f:
        json.dump(data, f, indent=4)


@blog_routers.post("/blog", tags=["BLOG"])
def create_blog(blog: BlogCreate):
    data = load_data()
    if any(p["id"] == blog.id for p in data):
        raise HTTPException(status_code=400, detail="Blog id already exist.")
    data.append(blog.model_dump())
    save_data(data)
    return blog


@blog_routers.get("/view_blogs/", tags=["BLOG"])
def read_all_blog():
    return load_data()


@blog_routers.get("/view_blogs/{id}", tags=["BLOG"])
def read_blog(id: int):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="Blog not found.")
    id = id - 1
    return data[id]


@blog_routers.put("/view_blogs/edit/{id}", tags=["BLOG"])
def edit_blog(id: int, blog: BlogCreate):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="Blog not found.")
    data[id - 1] = blog.model_dump()
    save_data(data)
    return blog


@blog_routers.delete("/view_blogs/remove/{id}", tags=["BLOG"])
def remove_blog(id: int):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="Blog not found.")
    data.pop(id - 1)
    save_data(data)
    return "Blog removed successfully"
