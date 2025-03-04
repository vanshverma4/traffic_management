# crud.py
from sqlalchemy.orm import Session
from app.models import Violation
from app.schemas import ViolationCreate

# Create a new violation entry
def create_violation(db: Session, violation: ViolationCreate):
    db_violation = Violation(
        vehicle_number=violation.vehicle_number,
        violation_type=violation.violation_type,
        image_url=violation.image_url,
    )
    db.add(db_violation)
    db.commit()
    db.refresh(db_violation)
    return db_violation

# Get all violations
def get_violations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Violation).offset(skip).limit(limit).all()

    
    # Add the new violation
