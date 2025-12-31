from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Patient Management System")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A Fully Functional API to manage patient records."}

# Create Patient
@app.post("/create")
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    if db.query(models.Patient).filter(models.Patient.id == patient.id).first():
        raise HTTPException(status_code=400, detail="Patient already exists")

    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()

    return {"message": "Patient created successfully"}

# View All Patients
@app.get("/view")
def view_patients(db: Session = Depends(get_db)):
    patients = db.query(models.Patient).all()
    return patients

# View Patient by ID
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# Update Patient
@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, update: schemas.PatientUpdate, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    for key, value in update.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)

    db.commit()
    return {"message": "Patient updated successfully"}

# Delete Patient
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str, db: Session = Depends(get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(patient)
    db.commit()
    return {"message": "Patient deleted successfully"}

# Sort Patients
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., regex="^(height|weight)$"),
    order: str = Query("asc", regex="^(asc|desc)$"),
    db: Session = Depends(get_db),
):
    column = getattr(models.Patient, sort_by)
    patients = db.query(models.Patient).order_by(
        column.desc() if order == "desc" else column.asc()
    ).all()
    return patients
