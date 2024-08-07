from sqlmodel import SQLModel, Field
from datetime import datetime


class Blog(SQLModel, table=True):
    id: int = Field(unique=True, primary_key=True)
    title: str = Field()
    content: str = Field()
    author_id: int = Field()
    author_name: str = Field()
    published_on: datetime = Field(datetime.utcnow)
