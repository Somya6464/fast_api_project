from fastapi import FastAPI, Depends, HTTPException, status, Request, Depends, Header
from fastapi.responses import JSONResponse
import models, schemas, services
from db import get_db, engine
from sqlalchemy.orm import Session

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

@app.get("/books/get_books", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
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

# USE OF HEADERS #
def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":    
        raise HTTPException(status_code=401, detail="Invalid token")
    return {
        "message": "Token is valid",
        "token": token
    }

@app.get("/secure-data")
def secure_data(data=Depends(verify_token)):
    return {
        "message": "This is secure data",
        "token": data["token"]
    }

# MIDDLEWERE , LOGGING MIDDLEWERE#
# logging middleware is used to track incoming and outgoing requests

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response status: {response.status_code}")
    return response
