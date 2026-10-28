import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_search_validation_error():
    """Prueba AC-01: Término muy corto debe retornar 400"""
    response = client.get("/api/customers/search?q=ab")
    assert response.status_code == 400
    assert response.json() == {"detail": "Search term must be at least 3 characters long."}

def test_search_success_match():
    """Prueba AC-02: Término válido retorna 200 con resultados"""
    response = client.get("/api/customers/search?q=lop")
    assert response.status_code == 200
    data = response.json()
    assert any(c["name"] == "Maria Lopez" and c["email"] == "mlopez@test.com" for c in data)

def test_search_no_results():
    """Prueba AC-03: Término sin coincidencias retorna 200 con lista vacía"""
    response = client.get("/api/customers/search?q=xyz")
    assert response.status_code == 200
    assert response.json() == []

def test_search_with_surrounding_spaces():
    """Prueba FR-03 / CR-01: Término con espacios circundantes retorna coincidencias válidas"""
    response = client.get("/api/customers/search?q=  lop  ")
    assert response.status_code == 200
    data = response.json()
    assert any(c["name"] == "Maria Lopez" and c["email"] == "mlopez@test.com" for c in data)

def test_search_validation_error_whitespace():
    """Prueba FR-06 / CR-01: Término con solo espacios o menor a 3 caracteres tras recorte retorna 400"""
    response = client.get("/api/customers/search?q=   ")
    assert response.status_code == 400
    assert response.json() == {"detail": "Search term must be at least 3 characters long."}

    response_padded_short = client.get("/api/customers/search?q=  ab  ")
    assert response_padded_short.status_code == 400
    assert response_padded_short.json() == {"detail": "Search term must be at least 3 characters long."}
