from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PatientCreate(BaseModel):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None

class PatientResponse(BaseModel):
    id: int
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None

    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    patient_id: int
    staff_id: int
    date: str
    purpose: Optional[str] = None

class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    staff_id: int
    date: str
    purpose: Optional[str] = None

    class Config:
        orm_mode = True
