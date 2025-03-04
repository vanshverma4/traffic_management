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




'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

# Define the database connection URL
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/traffic_management"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session maker bound to this engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Function to create tables
def create_tables():
    try:
        # Create all tables based on models
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created successfully!")
    except SQLAlchemyError as e:
        print(f"Error creating tables: {e}")

# If this script is run directly, create tables (useful for debugging)
if __name__ == "__main__":
    create_tables()
'''