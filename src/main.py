from fastapi import FastAPI, HTTPException, Query
from src.logic import filter_customers
from src.repository import load_customers

app = FastAPI(title="Customer Search API")

@app.get("/api/customers/search")
def search_customers(q: str = Query(..., description="Término de búsqueda")):
    """
    Endpoint de búsqueda.
    Orquesta el llamado a repository, logic y el manejo de errores (T-03).
    """
    try:
        customers = load_customers()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error reading data source.") from e

    try:
        return filter_customers(customers, q)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))