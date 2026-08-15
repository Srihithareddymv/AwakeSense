from fastapi import FastAPI
from backend.routes import router

app = FastAPI(
    title="AwakeSense",
    version="1.0.0",
    description="AI Powered Fatigue Monitoring System"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AwakeSense",
        "status": "Running"
    }
