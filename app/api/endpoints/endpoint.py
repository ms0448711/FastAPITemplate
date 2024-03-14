from fastapi import APIRouter
from app.schemas.endpoint import Endpoint
router = APIRouter()

@router.post("/webhook",response_model=Endpoint)
def endpoint(body:dict):
    print(body)
    return Endpoint(id="123")