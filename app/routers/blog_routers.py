from fastapi import APIRouter
from app.schemas.blog_schemas import BlogCreate

blog_routers = APIRouter()


data = []


@blog_routers.post("/post", tags=["BLOG"])
async def create_blog(blog: BlogCreate):
    data.append(blog.model_dump())
    return data


@blog_routers.get("/post/{id}", tags=["BLOG"])
def read_blog(id: int):
    id = id - 1
    return data[id]


@blog_routers.patch("/post/{id}", tags=["BLOG"])
def edit_blog(id: int, blog: BlogCreate):
    data[id - 1] = blog
    return data


@blog_routers.delete("/post/{id}", tags=["BLOG"])
def remove_blog(id: int):
    data.pop(id - 1)
    return data
