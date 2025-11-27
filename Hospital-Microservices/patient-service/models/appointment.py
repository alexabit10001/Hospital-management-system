from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from database import Base
import datetime

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, nullable=False)            # FK to patients.id (logical, not enforced here)
    staff_id = Column(Integer, nullable=False)              # staff id from staff-service
    date = Column(String(40), nullable=False)
    purpose = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
