# schemas.py
from pydantic import BaseModel
from typing import Optional

class ViolationBase(BaseModel):
    vehicle_number: str
    violation_type: str
    image_url: Optional[str] = None

class ViolationCreate(ViolationBase):
    pass

class Violation(ViolationBase):
    id: int
    created_at: str

    class Config:
        orm_mode = True

