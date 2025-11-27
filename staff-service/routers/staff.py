from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.staff import Staff
from schemas import StaffCreate, StaffResponse

router = APIRouter()

@router.post("/", response_model=StaffResponse)
def create_staff(staff: StaffCreate, db: Session = Depends(get_db)):

    new_staff = Staff(
        name=staff.name,
        role=staff.role,
        department=staff.department
    )

    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)

    return new_staff


@router.get("/{staff_id}", response_model=StaffResponse)
def get_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = db.query(Staff).filter(Staff.id == staff_id).first()

    if not staff:
        raise HTTPException(404, "Staff not found")

    return staff


@router.get("/", response_model=list[StaffResponse])
def list_staff(db: Session = Depends(get_db)):
    return db.query(Staff).all()
