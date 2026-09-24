# Customer Search Feature

## Goal
Implementar un endpoint HTTP `GET /api/customers/search` que permita buscar clientes por nombre o correo electrónico soportando coincidencias parciales[cite: 4].

## Requirements Covered
* FR-01, FR-02, FR-03, FR-04, FR-05, FR-06
* NFR-01, NFR-02, NFR-03

## Scope
* Creación del endpoint de búsqueda y lógica de filtrado[cite: 4].
* Lectura de datos desde un archivo JSON local en memoria.

## Out of Scope
* Autenticación o autorización de la API.
* Endpoints de mutación (POST, PUT, DELETE).

## Domain Model
* **Customer**: `{"id": int, "name": str, "email": str}`

## Search Rules
1. Parámetro de consulta esperado: `q` (string).
2. Se evalúa si `q` está contenido en `name` OR `email` de forma case-insensitive.

## Validation Rules
1. Si `len(q) < 3`, la API debe rechazar la petición.

## Error Handling
* Término corto: HTTP 400 Bad Request con detalle `{"detail": "Search term must be at least 3 characters long."}`.
* Falla al leer origen de datos: HTTP 500 Internal Server Error.

## Acceptance Criteria
* **AC-01 (Validación):** Dado un cliente HTTP, cuando envía un GET a `/api/customers/search?q=ab`, entonces recibe un HTTP 400.
* **AC-02 (Búsqueda exitosa):** Dado que existe "Maria Lopez" (mlopez@test.com), cuando se hace GET a `/api/customers/search?q=lop`, entonces recibe un HTTP 200 con el registro de Maria en la lista.
* **AC-03 (Sin resultados):** Dado que no hay coincidencias para "xyz", cuando se hace GET, entonces recibe HTTP 200 con un JSON `[]`.

## Test Scenarios
* Búsqueda por nombre exacto.
* Validación de longitud menor a 3.
* Comportamiento con lista vacía.