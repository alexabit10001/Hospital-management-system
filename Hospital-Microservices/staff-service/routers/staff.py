from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.staff import Staff
from schemas import StaffCreate, StaffResponse

router = APIRouter()

@router.post("/", response_model=StaffResponse)
def create_staff(payload: StaffCreate, db: Session = Depends(get_db)):
    s = Staff(name=payload.name, role=payload.role, department=payload.department)
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

@router.get("/{staff_id}", response_model=StaffResponse)
def get_staff(staff_id: int, db: Session = Depends(get_db)):
    s = db.query(Staff).filter(Staff.id == staff_id).first()
    if not s:
        raise HTTPException(404, "Staff not found")
    return s

@router.get("/", response_model=list[StaffResponse])
def list_staff(db: Session = Depends(get_db)):
    return db.query(Staff).all()
