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
