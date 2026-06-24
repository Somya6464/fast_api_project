from fastapi import FastAPI, Depends, HTTPException, status, Request, UploadFile, File, Header
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import models, schemas, services
from db import get_db, create_table
from sqlalchemy.orm import Session
import asyncio
from jose import jwt, JWTError, ExpiredSignatureError
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from typing import List, Optional
import os, shutil
from fastapi.staticfiles import StaticFiles
# from dotenv import load_dotenv
from config import settings

# Create tables
create_table()

app = FastAPI()

# load_dotenv()
 
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
SECRET_KEY = settings.origins
ALGORITHM = settings.ALGORITHM  # WE ALSO HAVE RS256, RS512, HS512, HS384, RS384, ES256, ES384, ES512
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


# password hashing #
# from passlib.context import CryptContext
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# File Upload #
#step 1: ensure upload folder exists
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# step 2: create endpoint for file upload
app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")

# step 3: create endpoint to handle file upload
@app.post("/uploadfile/")
def upload_file(file: UploadFile = File(...)):
    fileName = file.filename
    filePath = os.path.join(UPLOAD_DIR, fileName)

    if not fileName:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    with open(filePath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return {"filename": fileName, "message": "File uploaded successfully",
                "file_url": f"/files/{fileName}"} 
    
# step 4: Get file url api
def get_file(file_name: str):
    file_path = os.path.join(UPLOAD_DIR, file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return {"file_url": f"/files/{file_name}"}

@app.get("/files/{file_name}")
def read_file(file_name: str):
    return get_file(file_name)


# Implementation of CORS #
from fastapi.middleware.cors import CORSMiddleware

origins = os.getenv("origins")

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"], # allow for all methods and headers
    allow_headers = ["*"]
)
""" After this we can access api's from this port of frontend, but in mobile apps we don't need to use this."""

# Working 3rd party Api's  #
import requests


@app.get("/posts_list")
def get_posts_list():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()


# Implementing web crawling #
from bs4 import BeautifulSoup
@app.get("/web_crawling")
def web_crawling():
    url = "https://indianexpress.com/"
    
    # FIX 1: Add a User-Agent header so the website doesn't block you
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    # Optional: Check if the request was successful before parsing
    if response.status_code != 200:
        print(f"Failed to get page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    data = []
    for article in soup.find_all("a", class_="article-click topblockNews__sidebarLink"):
        title = article.text.strip()
        link = article.get("href") 
        if link and not link.startswith("http"):
            link = "https://indianexpress.com" + link
            
        data.append({"title": title, "link": link})
        
    return data 


# Pagination #
@app.get("/pagination")
def pagination(page: int = 1, limit: int = 5):
    url = "https://news.ycombinator.com/"
    
    # FIX 1: Add a User-Agent header so the website doesn't block you
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    # Optional: Check if the request was successful before parsing
    if response.status_code != 200:
        print(f"Failed to get page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    data = []
    for item in soup.find_all("span", class_="titleline"):
        title = item.text.strip()
        link = item.get("href") 
        if link and not link.startswith("http"):
            link = "https://indianexpress.com" + link
            
        data.append({"title": title, "link": link})
    # Implementing pagination logic
    start = (page - 1) * limit
    end = start + limit
        
    return {
"page": page, "limit": limit,
"total": len(data),
 "data": data[start:end]
    } 

# Caching #
import time

# store cache data
cache_data = []
last_fetch = 0

@app.get("/caching")
def caching():
    global cache_data, last_fetch
    # Check if cache is valid (e.g., 60 seconds)

    if last_fetch and (time.time() - last_fetch < 60) and cache_data:
        return {"message": "Data fetched from cache", "data": cache_data}

    url = "https://news.ycombinator.com/"
    
    # FIX 1: Add a User-Agent header so the website doesn't block you
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    # Optional: Check if the request was successful before parsing
    if response.status_code != 200:
        print(f"Failed to get page. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    data = []
    for item in soup.find_all("span", class_="titleline"):
        title = item.text.strip()
        link = item.get("href") 
        if link and not link.startswith("http"):
            link = "https://indianexpress.com" + link
            
        data.append({"title": title, "link": link})
        
    cache_data = data
    last_fetch = time.time()
    
    # FIX 6: Return the same dictionary structure as the cache for consistency
    return {"message": "Data fetched from web", "data": data}


# Rate limiting #
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


# limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Error handler
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"message": "Rate limit exceeded. Please try again later."},
    )

@app.get("/data_limit")
@limiter.limit("5/minute")  # Limit to 5 requests per minute
def data_limit(request: Request):
    return {"message": "This is a rate-limited endpoint."}
