from fastapi import APIRouter

from app.api.endpoints import endpoint


api_router = APIRouter()

api_router.include_router(endpoint.router)