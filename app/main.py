from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(
    title="Micro-Merchant Payment API",
    description="Backend API for merchant management & payment processing",
    version="0.1.0",
)

# Register API routers
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Micro-Merchant Payment API"}

@app.get("/healthcheck")
def healthcheck():
    return {"status": "healthy"}