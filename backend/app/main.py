from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import engine

app = FastAPI(
    title="AutoMind LK API",
    version="1.0.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["Content-Type"]
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AutoMind LK API"
    }


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AutoMind LK Backend"
    }

@app.get("/api/v1/ready")
def readiness_check():

    try:

        with engine.connect() as connection:

            connection.execute(text("SELECT 1"))

        return {
            "status": "ready",
            "database": "connected"
        }

    except SQLAlchemyError:

        raise HTTPException(
            status_code=503,
            detail="Database connection unavailable"
        )