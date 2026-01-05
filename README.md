# Django REST Project

This is a Django project built with **Django REST Framework (DRF)** that provides a full backend system with user authentication, registration, and a product management API.

## 🛠 Technologies Used
- Python 3.x
- Django 6.x
- Django REST Framework
- Simple JWT (for authentication)
- SQLite (default database)

## 📦 Project Structure

config/          # Django project settings and URLs  
core/            # Product management app  
    ├─ models.py  
    ├─ serializers.py  
    ├─ views.py  
    └─ urls.py  
Register/        # User registration app  
    ├─ serializers.py  
    ├─ views.py  
    └─ urls.py  
login/           # User login app  
    ├─ serializers.py  
    ├─ views.py  
    └─ urls.py  
db.sqlite3       # SQLite database  

## 🌟 Features

### Core App (`core`)
- Manage products (`Kala`) with the following fields:
  - `name`, `price`, `kind`, `status` (new/used), `descriptions`
- **API Endpoints** via `KalaView` (ModelViewSet):
  - GET: Accessible to anyone
  - POST/PUT/DELETE: Admin only
- Provides CRUD operations for products

### Register App (`Register`)
- User registration system
- **POST /register/** → create new users (accessible to all)
- **GET /register/** → list all users (admin only)
- Passwords are securely hashed using Django's `set_password`

### Login App (`login`)
- User login system
- **POST /login/** → authenticate users
- Validates username/password and active status
- Returns success message and username if login is successful
- GET requests are restricted to admin users

## 🔐 Authentication
- Uses **JWT authentication** via Simple JWT
- DRF default permissions: `IsAuthenticated` for protected endpoints

## 📌 API Endpoints

| Endpoint         | Method | Description                    | Permissions       |
|-----------------|--------|--------------------------------|-----------------|
| `/token`        | POST   | Obtain JWT token               | Public          |
| `/Refresh/`     | POST   | Refresh JWT token              | Public          |
| `/register/`    | POST   | Register new user              | Public          |
| `/register/`    | GET    | List all users                 | Admin only      |
| `/login/`       | POST   | User login                     | Public          |
| `/core/`        | GET    | List products                  | Public          |
| `/core/`        | POST   | Create new product             | Admin only      |
| `/core/<id>/`   | PUT    | Update product by ID           | Admin only      |
| `/core/<id>/`   | DELETE | Delete product by ID           | Admin only      |

## ⚡ How to Run

```bash
# 1. Clone the repository
git clone <your-repo-link>
cd <repo-folder>

# 2. Create virtual environment
python -m venv venv
# Activate
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# 3. Install dependencies
pip install django djangorestframework djangorestframework-simplejwt

# 4. Apply migrations
python manage.py migrate
instagram=amirali_zamani051
mygit=amiralizamani0511-tech

# 5. Run the server
python manage.py runserver
