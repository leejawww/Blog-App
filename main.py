from fastapi import FastAPI
from app.api.routers.blog_routers import blog_router
from app.api.routers.user_routers import user_router
from app.api.routers.auth_routers import auth_router


app = FastAPI(description="Blog Application")


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(blog_router)
