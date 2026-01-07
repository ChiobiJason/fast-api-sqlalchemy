from pydantic import BaseModel
from typing import Optional, List

# Pydantic Models (Dataclass)
class UserCreate(BaseModel):
    name: str
    email: str
    role: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True