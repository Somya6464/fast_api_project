from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books/get_books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_book():
    new_book = {
        "title": "Test Book",
        "author": "Test Author",
        "description": "This is a test book.",
        "year": 2024
    }
    response = client.post("/books/create_book", json=new_book)
    assert response.status_code == 201
    assert response.json()["title"] == new_book["title"]
    assert response.json()["author"] == new_book["author"]
    assert response.json()["description"] == new_book["description"]
    assert response.json()["year"] == new_book["year"]