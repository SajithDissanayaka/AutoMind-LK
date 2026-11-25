from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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