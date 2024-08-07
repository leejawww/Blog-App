from pydantic import BaseModel


class AuthUserCreate(BaseModel):
    # username: str = Field()
    id: int
    email: str
    password: str
