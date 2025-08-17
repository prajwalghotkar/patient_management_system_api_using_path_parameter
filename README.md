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

##### http://127.0.0.1:8000/docs#/default/muze_patient_ko_dekhana_hain_patient__patient_id__get
---
#### Using path function
```
from fastapi import FastAPI, Path
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
def muze_patient_ko_dekhana_hain(patient_id: str = Path(..., description='ID of the patient in the DataBase',example='P002')):
    # Load all the patients
    data = load_data()

    # Check if patient exists
    if patient_id in data:
        return data[patient_id]
    
    return {"error": f"Patient {patient_id} data main nahi hain"}
```
<img width="1920" height="985" alt="Screenshot 2025-08-17 003535" src="https://github.com/user-attachments/assets/aa1d7ba7-e58d-462c-858f-956c3ef47ceb" />

---

#### Code with HTTPException

![WhatsApp Image 2025-08-17 at 04 28 24_2314f657](https://github.com/user-attachments/assets/1447abc0-625b-4e6f-b81f-a640f1d9a3e8)

```
from fastapi import FastAPI, Path, HTTPException
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
def muze_patient_ko_dekhana_hain(patient_id: str = Path(..., description='ID of the patient in the DataBase',example='P002')):
    # Load all the patients
    data = load_data()

    # Check if patient exists
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient DataBase main hain hi nahi')
```

<img width="1920" height="911" alt="Screenshot 2025-08-17 042945" src="https://github.com/user-attachments/assets/8879087d-b323-462e-b4b9-4c03f8f0a954" />
<img width="1920" height="1022" alt="Screenshot 2025-08-17 042956" src="https://github.com/user-attachments/assets/391b8256-4caa-488a-a829-3fa29c8ee6d1" />
http://127.0.0.1:8000/docs#/default/muze_patient_ko_dekhana_hain_patient__patient_id__get

---

# 🏥 Patient Management System API (FastAPI + Query Parameters)

- The **Patient Management System API** is a lightweight RESTful API built with **FastAPI** that manages patient records efficiently.  
- This version demonstrates the use of **Query Parameters** to fetch and sort patient information.  
- It uses a **JSON file (`patients.json`) as the database**, making it easy to test, extend, and deploy.  

---

##### Tech Stack
- **Backend Framework:** FastAPI  
- **Language:** Python  
- **Database:** JSON file (`patients.json`)  
- **Server:** Uvicorn  

---

##### Project Structure
```
patient_management_system/
--> patients.json          # Database (Patient Records)
--> main.py                # FastAPI Application
--> README.md              # Documentation
```

---

#### API Endpoints

##### 1. Root Endpoint  
**GET /**  
Returns a welcome message.  
```json
{"message": "Patient Management System API (with Query Parameters)"}
```

---

##### 2. About Endpoint  
**GET /about**  
Describes the purpose of the API.  
```json
{"message": "This is the Patient Management System API, designed to manage patient records efficiently."}
```

---

##### 3. View All Patients  
**GET /view**  
Returns all patients stored in the database.  

Example Response:  
```json
{
  "P001": {"name": "Manaswi Sharma", "city": "New York City", "age": 28, "gender": "female", "bmi": 33.06, "verdict": "Obese"},
  "P002": {"name": "Prajwal Ghotkar", "city": "Los Angeles", "age": 35, "gender": "male", "bmi": 27.76, "verdict": "Overweight"}
}
```

---

##### 4. View Patient by ID (Query Parameter)  
**GET /patient?patient_id={id}**  

##### Example Request:  
```
/patient?patient_id=P002
```

##### Example Response:  
```json
{
  "name": "Prajwal Ghotkar",
  "city": "Los Angeles",
  "age": 35,
  "gender": "male",
  "height": 1.75,
  "weight": 85,
  "bmi": 27.76,
  "verdict": "Overweight"
}
```

 If patient doesn’t exist:  
```json
{"detail": "Patient DataBase main hain hi nahi"}
```

---

##### 5. Sort Patients (Query Parameters)  
**GET /sort?sort_by={field}&order={asc/desc}**  

- `sort_by`: **height | weight | bmi**  
- `order`: **asc (default) | desc**  

##### Example Request:  
```
/sort?sort_by=bmi&order=desc
```

##### Example Response (Top 2 shown):  
```json
[
  {"name": "Ava Martinez", "city": "Indianapolis", "age": 34, "gender": "female", "height": 1.66, "weight": 95, "bmi": 34.49, "verdict": "Obese"},
  {"name": "Rohan Patel", "city": "San Jose", "age": 45, "gender": "male", "height": 1.82, "weight": 110, "bmi": 33.20, "verdict": "Obese"}
]
```

---

##### Features
- Query Parameter usage (`/patient?patient_id=P002`)  
- Sort records dynamically by **height, weight, or BMI**  
- JSON-based lightweight data storage  
- Built-in validation & error handling with **HTTPException**  
- Includes BMI values with health verdicts (Normal, Overweight, Obese, Underweight)  

---
##### Code
```
from fastapi import FastAPI, Query, HTTPException
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
def muze_patient_ko_dekhana_hain(patient_id: str = Path(..., description='ID of the patient in the DataBase',example='P002')):
    # Load all the patients
    data = load_data()

    # Check if patient exists
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient DataBase main hain hi nahi')

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight, bmi"),
    order: str = Query("asc", description="Sort in asc or desc order")):

    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0),reverse=sort_order)

    return sorted_data
```

# Query Parameters  

Query parameters are optional key-value pairs appended to the end of a URL, used to pass additional data to the server in an HTTP request. They are typically employed for operations like filtering, sorting, searching, and pagination — without altering the endpoint path itself.  

**Example:**  
```
/patients?city=Delhi&sort_by=age
```

- The `?` marks the start of query parameters.  
- Each parameter is a key-value pair (`key=value`).  
- Multiple parameters are separated by `&`.  

### In this case:
- `city=Delhi` → is a query parameter for filtering.  
- `sort_by=age` → is a query parameter for sorting.  

---

## Query() in FastAPI  
`Query()` is a utility function provided by **FastAPI** to declare, validate, and document query parameters in your API endpoint.  

It allows you to:  
- Set default values  
- Enforce validation rules  
- Add metadata like description, title, example  

---

### Common Parameters in `Query()`  

- **default** --> Set default value (e.g., `Query(0)`)  
- **title** --> Displayed in API docs  
- **description** --> Detailed explanation in Swagger UI  
- **example / examples** --> Provide sample inputs  
- **min_length / max_length** --> Validate string length  
- **ge, gt, le, lt** --> Validate numeric bounds  
- **regex** --> Pattern match for strings  

---
### sorting on the basis of height
<img width="1920" height="907" alt="Screenshot 2025-08-17 053755" src="https://github.com/user-attachments/assets/cb248d59-63c0-415e-b945-99c22c3c9e03" />
---
### sorting on the basis of bmi
<img width="1920" height="955" alt="Screenshot 2025-08-17 053825" src="https://github.com/user-attachments/assets/ba76d9a2-c7d1-443a-a7bb-b54ae850f693" />


### http://127.0.0.1:8000/docs#/default/sort_patients_sort_get


