from fastapi import FastAPI
from app.routers import auth, users # IMPORTANT: import models
from app.db.database import Base, engine
from app.models import user  # import all models

app = FastAPI()


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
