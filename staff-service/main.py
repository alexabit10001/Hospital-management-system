from fastapi import FastAPI
from routers import staff
from database import engine, Base

app = FastAPI(
    title="Staff Service",
    description="Handles doctors, nurses & other staff",
    version="1.0"
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(staff.router, prefix="/staff", tags=["Staff"])

@app.get("/")
def root():
    return {"message": "Staff Service Running"}
