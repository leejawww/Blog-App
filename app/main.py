from fastapi import FastAPI
from .routers.blog_routers import blog_routers
from .routers.user_routers import user_routers

app = FastAPI()

app.include_router(user_routers)
app.include_router(blog_routers)
