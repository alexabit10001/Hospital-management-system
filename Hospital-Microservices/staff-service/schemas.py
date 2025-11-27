from pydantic import BaseModel
from typing import Optional

class StaffCreate(BaseModel):
    name: str
    role: str
    department: Optional[str] = None

class StaffResponse(BaseModel):
    id: int
    name: str
    role: str
    department: Optional[str] = None

    class Config:
        orm_mode = True
