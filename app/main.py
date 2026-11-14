from fastapi import FastAPI
# from routers.users import router as users_router
from app.routers.users import router as users_router

app = FastAPI(title="TaskboxAPI")

app.include_router(users_router)
