from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)
