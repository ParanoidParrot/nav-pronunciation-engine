from fastapi import FastAPI
from routes import router

app = FastAPI(title="Navigation Pronunciation API")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "running"}