from sqlmodel import SQLModel, Field
from datetime import datetime


class Blog(SQLModel):
    id: int = Field(unique=True, primary_key=True)
    title: str = Field()
    content: str = Field()
    author_id: int = Field()
    author_name: str = Field()
    published_on: datetime = Field()
