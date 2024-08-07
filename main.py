from fastapi import FastAPI
from app.api.v1.blog_routers import blog_router
from app.api.v1.user_routers import user_router
from app.api.v1.auth_routers import auth_router


app = FastAPI(description="Blog Application")


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(blog_router)
