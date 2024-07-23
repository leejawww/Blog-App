from fastapi import FastAPI
from .routers.blog_routers import blog_router
from .routers.user_routers import user_router
from .routers.auth_routers import auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(blog_router)
