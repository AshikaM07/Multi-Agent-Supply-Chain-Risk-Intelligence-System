
from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="Supply Chain Risk AI",
    version="1.0.0"
)

# Base API entry
app.include_router(health_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Supply Chain Risk AI Backend is running"}
