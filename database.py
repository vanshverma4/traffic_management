from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Define the database URL (make sure to use the correct credentials and DB name)
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/traffic_management"

# Create engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare base class for models
Base = declarative_base()

# Function to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
