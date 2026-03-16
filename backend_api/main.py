from fastapi import FastAPI
from backend_api.routes import router

app = FastAPI(title="Map Voice API")

app.include_router(router)

@app.get("/")
def health():
    return {"status": "running"}