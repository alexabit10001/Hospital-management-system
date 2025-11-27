from fastapi import FastAPI
from routers import patients, appointments
from database import Base, engine

app = FastAPI(title="Patient Service")

# create tables
Base.metadata.create_all(bind=engine)

app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

@app.get("/")
def root():
    return {"service": "patient-service", "status": "running"}
