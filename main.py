from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import models, schemas, services
from db import get_db, engine
from sqlalchemy.orm import Session
import asyncio
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Custom exception handler class
class UserNotFoundException(HTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=404, detail=detail)

# Global exception handler for UserNotFoundException
@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )
#async/await ka use aise hoga#
@app.get("/books/get_books", response_model=list[schemas.Book])
async def get_books(db: Session = Depends(get_db)):
    await asyncio.sleep(2)
    return services.get_book(db)

@app.get("/books/get_books/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = services.get_book_by_id(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# here we use the custom status code
@app.post("/books/create_book", response_model=schemas.Book, status_code=status.HTTP_201_CREATED) 
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)

@app.put("/books/update_book/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = services.update_book(db, book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@app.delete("/books/delete_book/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = services.delete_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


# IMPLEMENTATION OF DEPENDENCY INJECTION #
def common_logic():
    return{
        "message":"Common Logic executed"
    }

@app.get("/home")
def home(data= Depends(common_logic)):
    return data

# # USE OF HEADERS #
# def verify_token(token: str = Header(None)):
#     if token != "mysecrettoken":    
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return {
#         "message": "Token is valid",
#         "token": token
#     }

# @app.get("/secure-data")
# def secure_data(data=Depends(verify_token)):
#     return {
#         "message": "This is secure data",
#         "token": data["token"]
#     }

# MIDDLEWERE , LOGGING MIDDLEWERE#
# logging middleware is used to track incoming and outgoing requests

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response status: {response.status_code}")
    return response


# jwt implementation #
SECRET_KEY = "noSecretKey"
ALGORITHM = "HS256"  # WE ALSO HAVE RS256, RS512, HS512, HS384, RS384, ES256, ES384, ES512
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

class Token(BaseModel):
    access_token: str
    token_type: str

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "1234":
        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def verify_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credentials_exception
        return {"username": username}
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise credentials_exception

class BookListResponse(BaseModel):
    message: str
    data: List[schemas.Book]

@app.get("/books/get_books_jwt", response_model=BookListResponse)
async def get_books_jwt(
    db: Session = Depends(get_db),
    user: dict = Depends(verify_token),
):
    return {"message": "Token is valid", "data": services.get_book(db)}
