from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.appointment import Appointment
from schemas import AppointmentCreate, AppointmentResponse
from auth import verify_token
import httpx

router = APIRouter()

# URL for staff service - when running locally, staff runs on port 8001
STAFF_SERVICE_BASE = "http://localhost:8001/staff"

@router.post("/", response_model=AppointmentResponse)
async def create_appointment(payload: AppointmentCreate, db: Session = Depends(get_db), _=Depends(verify_token)):
    # Validate patient exists
    patient = db.execute("SELECT id FROM patients WHERE id = :id", {"id": payload.patient_id}).fetchone()
    if not patient:
        raise HTTPException(status_code=400, detail="Patient does not exist")

    # Call staff service to validate staff/doctor
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{STAFF_SERVICE_BASE}/{payload.staff_id}")
    if resp.status_code != 200:
        raise HTTPException(status_code=400, detail="Staff (doctor) not found in staff service")
    # Save appointment
    appt = Appointment(patient_id=payload.patient_id, staff_id=payload.staff_id, date=payload.date, purpose=payload.purpose)
    db.add(appt)
    db.commit()
    db.refresh(appt)
    return appt

@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appt = db.query(Appointment).filter(Appointment.id == appointment_id).first()
    if not appt:
        raise HTTPException(404, "Appointment not found")
    return appt

@router.get("/", response_model=list[AppointmentResponse])
def list_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()
