from pathlib import Path

from fastapi import FastAPI

from backend_api.routes import router
from backend_api.demo_page import get_demo_html

app = FastAPI(title="Map Voice API")

app.include_router(router)

@app.get("/")
def home():
    return get_demo_html()

@app.get("/demo")
def demo():
    return get_demo_html()

@app.get("/health")
def health():
    return {"status": "running"}