from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.profile_router import profile_router
from routers.skill_router import skill_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile_router)
app.include_router(skill_router)
