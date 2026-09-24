# Architecture

## Overview
Una API REST simple implementada con FastAPI que expone un endpoint de solo lectura para buscar registros de clientes almacenados en un archivo JSON estático.

## Components
1. **API Router (`main.py`)**: Define las rutas HTTP, extrae parámetros y formatea las respuestas HTTP.
2. **Search Logic (`logic.py`)**: Funciones puras que aplican las reglas de negocio sobre los datos (filtrado, validación).
3. **Data Repository (`repository.py`)**: Encargado de las operaciones de I/O, leyendo el archivo `data.json` y cargándolo en memoria.

## Data Flow
Cliente HTTP -> GET `/api/customers/search?q=term` -> `main.py` -> Valida longitud y llama a `logic.py` -> `logic.py` solicita datos a `repository.py` -> Retorna JSON filtrado -> Cliente HTTP.

## Testing Strategy
* Pruebas de integración sobre los endpoints usando `fastapi.testclient.TestClient` orquestado por `pytest`[cite: 4].