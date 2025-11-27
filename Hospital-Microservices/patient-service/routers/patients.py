from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.patient import Patient
from schemas import PatientCreate, PatientResponse
from auth import verify_token

router = APIRouter()

@router.post("/", response_model=PatientResponse)
def create_patient(payload: PatientCreate, db: Session = Depends(get_db), _=Depends(verify_token)):
    p = Patient(name=payload.name, age=payload.age, gender=payload.gender)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    p = db.query(Patient).filter(Patient.id == patient_id).first()
    if not p:
        raise HTTPException(404, "Patient not found")
    return p

@router.get("/", response_model=list[PatientResponse])
def list_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()
