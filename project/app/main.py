# project/app/main.py

from fastapi import Depends, FastAPI
from app.config import get_settings, Settings
app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
        }