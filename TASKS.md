# Tasks

## T-01 Data loading
* **Goal**: Implementar la lectura del archivo JSON para que retorne los clientes[cite: 4].
* **Files**: `src/repository.py`
* **Acceptance**: La función `load_customers()` lee correctamente `src/data.json` y retorna una lista de diccionarios.
* **Verification**: Pruebas unitarias o ejecución manual básica.

## T-02 Search and Validation logic
* **Goal**: Implementar la función de filtrado con las reglas de negocio[cite: 4].
* **Files**: `src/logic.py`
* **Acceptance**: La función lanza ValueError si el término es < 3 y retorna la lista filtrada de manera case-insensitive.
* **Verification**: Pruebas unitarias de la lógica pura.

## T-03 API Endpoint
* **Goal**: Exponer la lógica a través del endpoint HTTP GET `/api/customers/search`[cite: 4].
* **Files**: `src/main.py`
* **Acceptance**: El endpoint captura el query parameter `q`, maneja la excepción de validación retornando HTTP 400 y devuelve HTTP 200 con resultados válidos.
* **Verification**: Llamadas usando `curl` o Postman / Swagger UI.

## T-04 Automated Tests
* **Goal**: Implementar la suite de pruebas para cubrir los AC-01, AC-02 y AC-03[cite: 4].
* **Files**: `tests/test_api.py`
* **Acceptance**: Todas las pruebas con TestClient pasan exitosamente.
* **Verification**: Ejecución de `pytest -v`[cite: 4].