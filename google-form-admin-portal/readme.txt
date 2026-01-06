1. Features Present 

a. Multi-City Google Forms
b. Fetch Google Form responses city-wise
c. Store responses in MySQL
d. Manual Sync per city
e. Auto Sync every 1 hour
f. Admin Login
g. Admin Dashboard
h. Duplicate prevention (email + city)
i. Close all Google Forms with one button
j. Reopen all forms
k. Custom “Registration Closed” message
l. Anyone opening form link sees “Registration Closed”




2. Steps

Admin Dashboard (HTML + CSS + JS)
        |
        v
FastAPI Backend (Python)
        |
        v
Google Apps Script (Web App)
        |
        v
Google Forms + Google Sheets
        |
        v
MySQL Database





3. Tech Stack

a. Backend
     FastAPI
     SQLAlchemy
     MySQL
     APScheduler (auto sync)
     Requests

b. Frontend
     HTML
     CSS
     JavaScript (Fetch API)

c. Google
     Google Forms
     Google Sheets
     Google Apps Script





4. Database Schema
form_responses

id INT AUTO_INCREMENT PRIMARY KEY
full_name VARCHAR(255) NOT NULL
email VARCHAR(255) NOT NULL
mobile VARCHAR(50)
gender VARCHAR(50)
nationality VARCHAR(100)
city VARCHAR(100)
form_id VARCHAR(255)
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP





5. Google Sheet: FormRegistry

This sheet acts as the central registry.
city	form_id (Google Form ID)	sheet_id (Response Sheet ID)
Patna	xxxxxxxxxxxxxxxxxx	        yyyyyyyyyyyyyyyyyyyyyyy
Mumbai	xxxxxxxxxxxxxxxxxx	        yyyyyyyyyyyyyyyyyyyyyyy

⚠️ form_id must be the Google Form ID, not Sheet ID.





6. Google Apps Script (Key Responsibilities)

a. Fetch responses for a city
b. Open / Close all city forms
c. Set custom closed message
d. Validate and sanitize form IDs
e. Return JSON to FastAPI

Important:
The Google account running Apps Script must be Editor or Owner of all Google Forms.




7. How to Run Locally

a. Backend
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload

b. Frontend
    Open:
    frontend/index.html





8. Testing Endpoints

a. Sync City
    POST /sync/Patna

b. Close All Forms
    POST /forms/close-all

c. Open All Forms
    POST /forms/open-all



