# Micro-Merchant Payment API 

A production-ready, containerized backend API built with **FastAPI**, **SQLAlchemy ORM**, **PostgreSQL**, and **Docker** designed for micro-merchant onboarding, user authentication, and multi-provider payment processing (with webhook simulation).

---

##  Tech Stack

* **Framework:** FastAPI (Python 3.13)
* **Database & ORM:** PostgreSQL 16, SQLAlchemy 2.0, Alembic (migrations)
* **Validation & Settings:** Pydantic V2, `pydantic-settings`
* **Security:** JWT Authentication (`python-jose`), Passlib (bcrypt hashing)
* **Testing:** Pytest, TestClient
* **Containerization:** Docker & Docker Compose

---

##  Project Architecture


micro-merchant-api/
│
├── alembic/              # Database migration scripts
├── app/
│   ├── api/v1/           # API Routers (Auth, Merchants, Transactions, Webhooks)
│   ├── core/             # Security, Dependencies, Config settings
│   ├── models/           # SQLAlchemy Database Models (User, Merchant, Transaction)
│   ├── schemas/          # Pydantic V2 Request/Response validation schemas
│   ├── database.py       # DB Session & Base setup
│   └── main.py           # FastAPI application entrypoint
│
├── tests/                # Automated Pytest suite (SQLite in-memory)
├── .env.example          # Environment variable template
├── Dockerfile            # Production container build definition
├── docker-compose.yml    # Multi-service cluster config (App, DB, Adminer)
└── requirements.txt      # Project dependencies


## Local Development & Testing

### 1. Clone & Set Up Virtual Environment
git clone https://github.com/TheDarkknight2200/micro-merchant-api.git
cd micro-merchant-api

python -m venv venv
venv\Scripts\activate  # On macOS/Linux use: source venv/bin/activate
pip install -r requirements.txt

### 2. Configure Environment Variables
Create a .env file in the root directory:
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your_super_secret_jwt_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

### 3. Run Automated Tests
pytest

---

## Running with Docker (Production Stack)

### 1. Build and Start the Containers
docker-compose up --build -d

### 2. Run Database Migrations
docker-compose exec web alembic upgrade head

### 3. Access the Services
- Interactive API Docs (Swagger UI): http://localhost:8000/docs
- Adminer DB Management UI: http://localhost:8080 (System: PostgreSQL, Server: db, Username: postgres, Password: postgres, Database: merchant_db)

---

## API Endpoints Overview

- POST /api/v1/auth/register - Register a new user/owner (No Auth)
- POST /api/v1/auth/login - Authenticate and receive JWT access token (No Auth)
- POST /api/v1/merchants/ - Onboard a new micro-merchant profile (Bearer Auth)
- POST /api/v1/transactions - Initiate a payment transaction (Bearer Auth)
- GET /api/v1/transactions/merchant/{id} - Retrieve paginated transactions (Bearer Auth)
- POST /api/v1/webhooks/payment-callback - Async webhook handler for payment providers (No Auth)

---

## License
Distributed under the MIT License.