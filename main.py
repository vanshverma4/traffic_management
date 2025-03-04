# main.py
from app.database import engine, Base, get_db
from app import models, crud, schemas
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List  # Import List from typing


# Create tables in the database (run this once)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Create a new violation entry
@app.post("/violations/", response_model=schemas.Violation)
def create_violation(violation: schemas.ViolationCreate, db: Session = Depends(get_db)):
    return crud.create_violation(db=db, violation=violation)

# Get all violations
@app.get("/violations/", response_model=List[schemas.Violation])
def get_violations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_violations(db=db, skip=skip, limit=limit)
