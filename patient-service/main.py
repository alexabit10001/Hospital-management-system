from fastapi import FastAPI
from routers import patients, appointments
from database import engine, Base

app = FastAPI(
    title="Patient Service",
    description="Handles patient data + appointments",
    version="1.0"
)

# Create all tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])

@app.get("/")
def root():
    return {"message": "Patient Service Running"}
