from fastapi import APIRouter, HTTPException, Depends
from app.schemas.blog_schemas import BlogCreate
from app.models.blog_models import Blog
from app.routers.auth_routers import JWTBearer
from app.database.database import get_db
from sqlalchemy.orm import Session
import json
import os

from typing import List


blog_router = APIRouter(tags=["BLOG"])

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


@blog_router.post(
    "/blog",
    dependencies=[Depends(JWTBearer())],
    response_model=BlogCreate,
)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(**blog.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@blog_router.get("/view_blogs/", response_model=List[BlogCreate])
def read_all_blogs(db: Session = Depends(get_db)):
    results = db.query(Blog).all()
    return results


@blog_router.get("/view_blogs/{id}", response_model=BlogCreate)
def read_blog(id: int, db: Session = Depends(get_db)):
    results = db.query(Blog)
    id = id - 1
    return results[id]

    # data = load_data()
    # if id < 1 or id > len(data):
    #     raise HTTPException(status_code=404, detail="Blog not found.")
    # id = id - 1
    # save_data(data)
    # return data[id]


@blog_router.put("/view_blogs/edit/{id}", response_model=BlogCreate)
def edit_blog(id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    # blog_query = db.query(Blog).filter(Blog.id == id)
    # blog_query.update(blog.model_dump(), synchronize_session=False)
    # db.commit()
    # return blog_query.first()

    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="Blog not found.")
    id = id - 1
    save_data(data)
    return blog


@blog_router.delete("/view_blogs/remove/{id}")
def remove_blog(id: int, db: Session = Depends(get_db)):
    data = load_data()
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="Blog not found.")
    data.pop(id - 1)
    save_data(data)
    return "Blog removed successfully"
