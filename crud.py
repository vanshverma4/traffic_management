from sqlalchemy.orm import Session
from app.models import Violation
from app.schemas import ViolationCreate

# Create a new violation entry, including image URL
def create_violation(db: Session, violation: ViolationCreate):
    db_violation = Violation(
        vehicle_number=violation.vehicle_number,
        violation_type=violation.violation_type,
        image_url=violation.image_url,  # Save the image URL in the database
    )
    db.add(db_violation)
    db.commit()
    db.refresh(db_violation)
    return db_violation

# Get all violations with pagination
def get_violations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Violation).offset(skip).limit(limit).all()

