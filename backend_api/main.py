import os
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Header

API_KEY = os.getenv("API_KEY")


def get_api_key(api_key: str = Header(...)):
    """Dependency to check API key."""
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")


app = FastAPI()
secure_router = APIRouter(dependencies=[Depends(get_api_key)])
# secure_router.include_router(router_endpoint.router, prefix="/router_endpoint")
app.include_router(secure_router)


@app.get("/")
async def root():
    return "Welcome to the API!"
