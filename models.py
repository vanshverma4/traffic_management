from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Violation(Base):
    __tablename__ = 'violations'
    __table_args__ = {'extend_existing': True}  # Allow altering the existing table (optional)

    id = Column(Integer, primary_key=True, index=True)
    vehicle_number = Column(String, index=True, nullable=False)
    violation_type = Column(String, nullable=False)
    image_url = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
