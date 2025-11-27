Hospital Microservices demo
==========================

This project contains two independent FastAPI microservices:

1. patient-service (port 8000)
2. staff-service (port 8001)

Each service uses its own SQLite database (for easy local testing).
They communicate via REST: patient-service calls staff-service to validate staff when creating appointments.

How to run (locally)
--------------------
1. Create virtualenv and install deps for each service:
   - cd patient-service
   - python -m venv .venv
   - source .venv/bin/activate   (or .venv\Scripts\activate on Windows)
   - pip install -r requirements.txt
   - uvicorn main:app --reload --port 8001   # for staff-service

   In a second terminal:
   - cd patient-service
   - install deps and run:
   - uvicorn main:app --reload --port 8000

2. Create a JWT token (simple helper in patient-service/auth.py). For quick testing you can temporarily comment out token dependency.

Notes
-----
- This is a demo using SQLite for convenience. To use MySQL, change DATABASE_URL to your MySQL connection string in database.py files and install pymysql, then create the DBs.
