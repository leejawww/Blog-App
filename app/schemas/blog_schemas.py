from pydantic import BaseModel


class BlogCreate(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    author_name: str
    published_on: str
