from fastapi import FastAPI, Depends, File, UploadFile
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app import models, crud, schemas
from typing import List
import os
from pathlib import Path
from fastapi.staticfiles import StaticFiles

# Create tables in the database (run this once)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Directory to save uploaded files
UPLOAD_DIRECTORY = Path("uploads")

if not UPLOAD_DIRECTORY.exists():
    UPLOAD_DIRECTORY.mkdir()

# Serve uploaded images as static files
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIRECTORY), name="uploads")

# Endpoint to handle image upload along with violation data
@app.post("/violations/", response_model=schemas.Violation)
async def create_violation(
    vehicle_number: str,
    violation_type: str,
    file: UploadFile = File(...),  # Use UploadFile to handle file uploads
    db: Session = Depends(get_db)
):
    # Save the image to the uploads directory
    image_path = UPLOAD_DIRECTORY / file.filename
    with open(image_path, "wb") as f:
        f.write(await file.read())

    # Create the image URL to store in the database
    image_url = f"/uploads/{file.filename}"  # Use relative URL for static file

    # Create a new violation entry in the database, including the image URL
    violation = schemas.ViolationCreate(
        vehicle_number=vehicle_number,
        violation_type=violation_type,
        image_url=image_url,
    )
    return crud.create_violation(db=db, violation=violation)

# Endpoint to get all violations
@app.get("/violations/", response_model=List[schemas.Violation])
def get_violations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_violations(db=db, skip=skip, limit=limit)
