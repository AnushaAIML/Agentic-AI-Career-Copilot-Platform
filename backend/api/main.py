from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes.chat import router as chat_router
from backend.api.routes.resume import router as resume_router
from backend.api.routes.jd_match import router as jd_router
from backend.api.routes.interview import router as interview_router
#from backend.api.routes.career import router as career_router

app = FastAPI(
    title="Agentic Career Platform"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(resume_router)
app.include_router(jd_router)
app.include_router(interview_router)
# app.include_router(career_router)


@app.get("/")
def root():

    return {
        "message":
        "Agentic Career Platform API Running"
    }