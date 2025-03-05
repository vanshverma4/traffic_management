from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ViolationBase(BaseModel):
    vehicle_number: str
    violation_type: str
    image_url: Optional[str] = None  # This will store the URL of the uploaded image

class ViolationCreate(ViolationBase):
    pass  # This will be used for creating a violation entry (same fields as ViolationBase)

class Violation(ViolationBase):
    id: int
    created_at: datetime  # Using datetime for the creation timestamp

    class Config:
        orm_mode = True  # This tells Pydantic to treat ORM models as dictionaries, which is important for SQLAlchemy.
