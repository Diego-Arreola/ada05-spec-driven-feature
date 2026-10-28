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

def test_search_with_surrounding_whitespace():
    """Prueba CR-01 / FR-03: Término con espacios circundantes retorna coincidencias correctamente tras trim"""
    response = client.get("/api/customers/search?q=  lop  ")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(c["name"] == "Maria Lopez" and c["email"] == "mlopez@test.com" for c in data)

def test_search_whitespace_only_validation_error():
    """Prueba CR-01 / FR-06: Término con espacios insuficientes o solo espacios debe retornar 400"""
    response = client.get("/api/customers/search?q=   ")
    assert response.status_code == 400
    assert response.json() == {"detail": "Search term must be at least 3 characters long."}
