from fastapi import FastAPI

from . import models, schemas
from .database import engine
from .routers import authentication, blog, user

app = FastAPI()

# 自動でテーブルが作成される
models.Base.metadata.create_all(engine)

# APIのルーターを別ファイルに定義
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
