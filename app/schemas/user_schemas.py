from pydantic import BaseModel


class UserCreate(BaseModel):
    id: int
    username: str
    email: str
    password: str
