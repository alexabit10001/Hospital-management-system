from fastapi import FastAPI
from routers import staff
from database import Base, engine

app = FastAPI(title="Staff Service")
Base.metadata.create_all(bind=engine)

app.include_router(staff.router, prefix="/staff", tags=["Staff"])

@app.get("/")
def root():
    return {"service": "staff-service", "status": "running"}
