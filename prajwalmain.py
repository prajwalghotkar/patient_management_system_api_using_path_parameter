from fastapi import FastAPI, Query, HTTPException
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as prajwal_file:
        data = json.load(prajwal_file)
    return data    

@app.get("/")
def read_root():
    return {"message": "Patient Management System API (with Query Parameters)"}

@app.get('/about')
def about():
    return {'message': 'This is the Patient Management System API, designed to manage patient records efficiently.'}

@app.get('/view')
def view():
    data = load_data()
    return data

# ✅ Query Parameter instead of Path Parameter
@app.get("/patient")
def muze_patient_ko_dekhana_hain(
    patient_id: str = Query(..., description="ID of the patient in the database", example="P002")
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient DataBase main hain hi nahi")

# ✅ Sorting Endpoint
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight, bmi"),
    order: str = Query("asc", description="Sort in asc or desc order")
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")
    
    data = load_data()

    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
