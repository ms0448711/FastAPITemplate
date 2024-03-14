from typing import Optional

from pydantic import BaseModel

class Endpoint(BaseModel):
    id:str
    