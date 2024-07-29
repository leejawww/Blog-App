from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(unique=True, primary_key=True)
    username: str = Field()
    email: str = Field()
    password: str = Field()
