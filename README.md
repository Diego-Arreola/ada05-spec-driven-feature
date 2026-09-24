# Customer Search API

API REST construida con FastAPI que permite buscar clientes por nombre o correo electrónico soportando coincidencias parciales (case-insensitive) y validación de longitud mínima de búsqueda.

## Requisitos Previos

* Python 3.11+

## Instalación

1. Clona o descarga el repositorio y colócate en la raíz del proyecto:
   ```bash
   cd ada05-spec-driven-feature
   ```

2. (Opcional) Crea y activa un entorno virtual:
   * **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. Instala las dependencias necesarias:
   ```bash
   pip install fastapi uvicorn httpx pytest
   ```

## Ejecución

1. Inicia el servidor de desarrollo con `uvicorn`:
   ```bash
   uvicorn src.main:app --reload
   ```

2. La API estará disponible en `http://127.0.0.1:8000`.
   * **Documentación interactiva (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   * **Documentación alternativa (ReDoc):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Ejemplos de Búsqueda

* **Búsqueda exitosa (coincidencia parcial en nombre o correo):**
  ```bash
  curl "http://127.0.0.1:8000/api/customers/search?q=lop"
  ```
  Respuesta:
  ```json
  [
    {
      "id": 1,
      "name": "Maria Lopez",
      "email": "mlopez@test.com"
    }
  ]
  ```

* **Validación de longitud mínima (< 3 caracteres):**
  ```bash
  curl -i "http://127.0.0.1:8000/api/customers/search?q=ab"
  ```
  Respuesta (HTTP 400 Bad Request):
  ```json
  {
    "detail": "Search term must be at least 3 characters long."
  }
  ```

* **Sin coincidencias:**
  ```bash
  curl "http://127.0.0.1:8000/api/customers/search?q=xyz"
  ```
  Respuesta (HTTP 200 OK):
  ```json
  []
  ```

## Pruebas

Para ejecutar la suite de pruebas automatizadas con `pytest`:

* **Windows (PowerShell):**
  ```powershell
  $env:PYTHONPATH="."
  pytest -v
  ```
  o alternativamente:
  ```powershell
  python -m pytest -v
  ```

* **Linux / macOS:**
  ```bash
  PYTHONPATH=. pytest -v
  ```
