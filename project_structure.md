<!-- Inductry standart folder structure -->
my_fastapi_project/
│
├── alembic/                  # Database migrations (SQLAlchemy)
│   └── versions/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app instance, CORS, aur routers include karne ke liye
│   │
│   ├── core/                 # App ki core settings aur configurations
│   │   ├── __init__.py
│   │   ├── jwt.py
│   │   ├── config.py         # Pydantic BaseSettings (.env file read karne ke liye)
│   │   ├── security.py       # JWT token creation/verification, password hashing (passlib/bcrypt)
│   │   └── database.py       # SQLAlchemy engine, SessionLocal, Base
│   │
│   ├── models/               # SQLAlchemy Database Models (Tables)
│   │   ├── __init__.py
│   │   ├── user.py           # User model (with roles: admin, user)
│   │   ├── book.py           # Book model
│   │   └── otp.py            # OTP model (agar DB me store kar rahe hain)
│   │
│   ├── schemas/              # Pydantic Models (Request/Response validation)
│   │   ├── __init__.py
│   │   ├── user.py           # UserCreate, UserLogin, UserResponse, Token
│   │   ├── book.py           # BookCreate, BookUpdate, BookResponse
│   │   └── otp.py            # OTPVerify schema
│   │
│   ├── api/                  # API Endpoints (Routers)
│   │   ├── __init__.py
│   │   ├── deps.py           # Dependencies (get_current_user, role_checker, get_db)
│   │   └── v1/               # API Versioning (v1, v2...)
│   │       ├── __init__.py
│   │       ├── router.py     # Main router jo sabko combine karega
│   │       ├── auth.py       # Signup, Login, OTP verify endpoints
│   │       ├── users.py      # User profile, role management endpoints
│   │       └── books.py      # Existing Book CRUD endpoints
│   │
│   ├── crud/                 # Database Operations (Create, Read, Update, Delete logic)
│   │   ├── __init__.py
│   │   ├── user.py           # DB queries for users
│   │   └── book.py           # DB queries for books
│   │
│   ├── services/             # Business Logic (Complex operations)
│   │   ├── __init__.py
│   │   ├── auth_service.py   # OTP generation, validation, signup flow logic
│   │   └── book_service.py   # Book related complex business logic (if any)
│   │
│   └── utils/                # Helper functions & Third-party integrations
│       ├── __init__.py
│       ├── email.py          # SMTP / SendGrid / Resend integration for sending OTP
│       └── helpers.py        # General utility functions
│
├── tests/                    # Pytest test cases
│   ├── test_auth.py
│   └── test_books.py
│
├── .env                      # Environment variables (DB URL, JWT Secret, SMTP creds)
├── .gitignore
├── requirements.txt          # Dependencies
├── alembic.ini               # Alembic config
└── README.md


<!-- purpose of each folder and file -->

🧠 Har Folder ka Purpose (Detail me samjhein):
1. app/core/ (Configuration & Security)
config.py: Yahan pydantic-settings ka use karke .env file se variables (DB URL, JWT Secret Key, Email Password) load honge.
security.py: Yahan aapke JWT Token banane (create_access_token) aur verify karne ka code hoga. Password hash karne ke liye passlib ka setup yahan rahega.
database.py: Database connection aur session management.
2. app/models/ & app/schemas/
models/: Yahan aapke Database tables banenge. User model me aapko ek role column (e.g., Enum('admin', 'user')) aur is_verified (boolean for OTP) add karna hoga.
schemas/: Yahan Pydantic models honge jo API request/response ko validate karenge. (e.g., Token schema jisme access_token aur token_type hoga).
3. app/api/deps.py (Sabse Important for your requirement)
Kyunki aapko existing APIs me token pass karna hai aur role-based access chahiye, yeh file aapka Gatekeeper hogi.
4. app/api/v1/books.py (Existing APIs me Token kaise add karein?)
Ab aapke existing book endpoints me deps.py ka use karke token verify karenge:
5. app/services/ & app/utils/ (Email OTP Logic)
utils/email.py: Yahan aap smtplib ya koi third-party service (SendGrid, Resend, AWS SES) ka code likhenge jo actual me email bhejega.
services/auth_service.py: Signup ka flow yahan manage hoga.
User data save karein (is_verified=False).
6-digit OTP generate karein.
utils/email.py call karke OTP bhejein.
OTP ko cache (Redis) ya DB me temporary store karein.
6. app/api/v1/auth.py (Auth Endpoints)
Yahan aapke authentication routes honge:
POST /signup -> OTP bhejega.
POST /verify-otp -> User ko verify karega aur JWT token return karega.
POST /login -> Email/Password check karke token dega.