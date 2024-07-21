from sqlmodel import SQLModel, Field


class Blog(SQLModel):
    id: int = Field(unique=True, primary_key=True)
    title: str = Field()
    content: str = Field()
    description: str = Field()
    author_id: int
    author_name: str
    published_on: str
