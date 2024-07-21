from pydantic import BaseModel
from datetime import datetime


class BlogCreate(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    author_name: str
    published_on: datetime
