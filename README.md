Health Information System — API Documentation & Feature Report
📌 Project Overview
This Health Information System is a secure and scalable Django-based application designed to enable medical professionals (e.g., doctors) to manage health programs and client enrollments. It features a RESTful API for easy integration with external systems and supports JWT-based authentication for access control.

🚀 Features
✅ 1. Create a Health Program
Doctors can create and manage various health programs such as:

HIV

Malaria

Tuberculosis

Endpoint:
POST /api/programs/
Authentication: Required

✅ 2. Register a New Client
Doctors can register clients by capturing:

Full name

Age

Contact information

Endpoint:
POST /api/clients/
Authentication: Required

✅ 3. Enroll a Client in One or More Programs
Clients can be enrolled in multiple health programs dynamically.

Endpoint:
POST /api/clients/{id}/enroll/
Body:

json
Copy
Edit
{
  "program_ids": [1, 2]
}
Authentication: Required

✅ 4. Search for Clients by Name
Quick search capability to locate clients using partial or full names.

Endpoint:
GET /api/clients/search/?name=Jane
Authentication: Required

✅ 5. View Client Profile with Programs
Doctors can view a detailed profile of a specific client, including all enrolled health programs.

Endpoint:
GET /api/clients/{id}/
Authentication: Required

✅ 6. Expose Client Profile via REST API
All features are accessible via a RESTful API and secured with JWT tokens.

API Base:
http://127.0.0.1:8000/api/

🔐 7. JWT-Based Security
Secure login and token-based session handling for API consumers (doctors/admins).

Obtain Token
POST /api/token/
Body:

json
Copy
Edit
{
  "username": "njange",
  "password": "4044"
}
Use Bearer Token
Include the token in request headers:

makefile
Copy
Edit
Authorization: Bearer <access_token>
🛠️ Technology Stack

Layer	Tech
Backend	Django (v4+)
API Framework	Django REST Framework
Auth	JWT (SimpleJWT)
Database	PostgreSQL
Docs/Test	Postman + DRF Browsable UI
📁 Project Structure
graphql
Copy
Edit
health_system/
├── core/
│   ├── models.py         # Client & Program models
│   ├── serializers.py    # API serializers
│   ├── views.py          # API views with permissions
│   ├── urls.py           # App URL routes
├── health_system/
│   ├── settings.py       # Project settings
│   ├── urls.py           # Global URL routes
🧪 API Testing Instructions
Start Server

bash
Copy
Edit
python manage.py runserver
Authenticate with JWT

http
Copy
Edit
POST /api/token/
Add Token in Postman Headers

makefile
Copy
Edit
Authorization: Bearer <access_token>
Use the following endpoints to:

GET/POST /api/clients/

GET/POST /api/programs/

POST /api/clients/{id}/enroll/

GET /api/clients/search/?name=...

GET /api/clients/{id}/

🔐 Security Considerations
JWT ensures only authenticated users can access or modify records.

No sensitive data is exposed in public APIs.

Future enhancements could include audit logs and field-level encryption.