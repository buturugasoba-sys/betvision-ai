from fastapi import FastAPI from .ai_router import router

app = FastAPI(
    title="BetVision AI API",
    description="AI sports analysis platform",
    version="0.1"
)


@app.get("/")
def home():
    return {
        "message": "BetVision AI API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }
