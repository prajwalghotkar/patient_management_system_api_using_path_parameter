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



##### Future Enhancements
- Add POST endpoint to insert new patients
- Add PUT and DELETE for full CRUD operations
- Connect to a real database (SQLite / MySQL / PostgreSQL)
- Add authentication for secure access 
