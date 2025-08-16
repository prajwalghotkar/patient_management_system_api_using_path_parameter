# 🏥 Patient Management System API (FastAPI + Path Parameter)
- The Patient Management System API is a lightweight RESTful API built with FastAPI to efficiently manage patient health records.
- It uses a JSON file as the database and demonstrates how to handle path parameters in APIs.
---
##### This project allows users to:

- View all patient records
- Fetch specific patient details using their Patient ID
- Learn about the API purpose via an /about endpoint
- Use a structured and scalable approach to manage health-related data
---
##### Tech Stack
- **Backend Framework**: FastAPI
- **Database**: JSON file (patients.json)
- **Language**: Python
- **Server**: Uvicorn

---
##### Project Structure

patient_management_system/
--> patients.json          # Database (Patient Records)
--> prajwalmain.py         # FastAPI Application
--> README.md              # Documentation

---
#### API Endpoints

##### 1) Root Endpoint
###### GET /
###### Returns a welcome message.
```
{"message": "Patient Management System API"}
```
---
##### 2) About Endpoint

###### GET /about
###### Describes the purpose of the API.
```
{"message": "This is the Patient Management System API, designed to manage patient records efficiently."}
```
---
##### 3) View All Patients

###### GET /view
###### Returns all patients stored in the database.
```
{
  "P001": {"name": "Manaswi Sharma", "city": "New York City", "age": 28, "gender": "female", "bmi": 33.06, "verdict": "Obese"},
  "P002": {"name": "Prajwal Ghotkar", "city": "Los Angeles", "age": 35, "gender": "male", "bmi": 27.76, "verdict": "Overweight"},
  ...
}
```
##### 4) View Patient by ID (Path Parameter)

###### GET /patient/{patient_id}
###### Fetch details of a specific patient using their patient_id.
###### Example Request:
```
GET /patient/P003
```
###### Example Response:
```
{
  "name": "Jully Smith",
  "city": "Chicago",
  "age": 22,
  "gender": "female",
  "height": 1.60,
  "weight": 45,
  "bmi": 17.58,
  "verdict": "Underweight"
}
```
###### If patient doesn’t exist:
```
{"error": "Patient P050 data main nahi hain"}
```
---
##### Features

- Path Parameter usage (/patient/{patient_id})
- JSON-based data storage (lightweight, easy to extend)
- API endpoints to manage and fetch patient data
- BMI included with health verdicts (Normal, Overweight, Obese, Underweight)
---
##### How to Run
```
from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as prajwal_file:
        data = json.load(prajwal_file)
    return data    

@app.get("/")
def read_root():
    return {"message": "Patient Management System API"}

@app.get('/about')
def about():
    return {'message': 'This is the Patient Management System API, designed to manage patient records efficiently.'}

@app.get('/view')
def view():
    data = load_data()

    return data

@app.get("/patient/{patient_id}")
def muze_patient_ko_dekhana_hain(patient_id: str):
    # Load all the patients
    data = load_data()

    # Check if patient exists
    if patient_id in data:
        return data[patient_id]
    
    return {"error": f"Patient {patient_id} data main nahi hain"}
```
<img width="1920" height="994" alt="Screenshot 2025-08-17 001306" src="https://github.com/user-attachments/assets/ec222bac-4e1e-4ebb-92d4-cc07d7855d24" />
<img width="1920" height="945" alt="Screenshot 2025-08-17 001543" src="https://github.com/user-attachments/assets/a2b88d08-d1b1-46bb-8caf-e710a228a566" />
<img width="1920" height="967" alt="Screenshot 2025-08-17 001621" src="https://github.com/user-attachments/assets/6e5358f0-7bdc-46b6-8514-57ee27d6241c" />
<img width="1920" height="967" alt="Screenshot 2025-08-17 001632" src="https://github.com/user-attachments/assets/a3b36c9f-ca61-4747-af0f-3cfcf64ec955" />


##### Future Enhancements
- Add POST endpoint to insert new patients
- Add PUT and DELETE for full CRUD operations
- Connect to a real database (SQLite / MySQL / PostgreSQL)
- Add authentication for secure access 

http://127.0.0.1:8000/docs#/default/muze_patient_ko_dekhana_hain_patient__patient_id__get
---
##### Using path function

