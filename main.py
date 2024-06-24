from fastapi import FastAPI
import logging

from config import SETTINGS
from dependencies import lifespan

logging.info(f"initializing app with settings: {SETTINGS}")

app = FastAPI(
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

@app.get("/health-check")
def view_health():
    return "OK"
