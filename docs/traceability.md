# Traceability Matrix

| Requirement | SPEC/AC | Task | Files | Test | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FR-01** | AC-02 | T-03 | `src/main.py` | `test_search_success_match` | Completed | Endpoint `/api/customers/search` expuesto con FastAPI |
| **FR-02** | AC-02 | T-02 | `src/logic.py` | `test_search_success_match` | Completed | Búsqueda por `name` y `email` |
| **FR-03** | AC-02 | T-02 | `src/logic.py` | `test_search_success_match` | Completed | Coincidencia parcial e insensible a mayúsculas |
| **FR-04** | AC-02 | T-01 | `src/repository.py` | `test_search_success_match` | Completed | Carga de clientes con estructura `id`, `name`, `email` desde JSON |
| **FR-05** | AC-03 | T-03 | `src/main.py` | `test_search_no_results` | Completed | Retorna HTTP 200 con `[]` |
| **FR-06** | AC-01 | T-02, T-03 | `src/logic.py`, `src/main.py` | `test_search_validation_error` | Completed | Requiere `>=3` caracteres, retorna HTTP 400 |
| **NFR-01**| N/A | T-01..T-03 | `src/main.py` | All Tests | Completed | API REST desarrollada en Python 3.11 con FastAPI |
| **NFR-02**| N/A | T-02 | `src/logic.py` | `test_search_success_match` | Completed | Ejecución en memoria local (<200ms) |
| **NFR-03**| N/A | T-01 | `src/repository.py` | `test_search_success_match` | Completed | Lectura de archivo `src/data.json` local sin BD externa |