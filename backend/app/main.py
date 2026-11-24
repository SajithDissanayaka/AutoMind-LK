from fastapi import FastAPI

app = FastAPI(
    title="AutoMind LK API",
    version="1.0.0"
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