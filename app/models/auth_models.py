from sqlmodel import SQLModel, Field


class AuthUser(SQLModel, table=True):
    # username: str = Field()
    id: int = Field(primary_key=True)
    email: str = Field()
    password: str = Field()
