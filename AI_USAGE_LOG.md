# AI Usage Log

### Entrada 01: Configuración de la persistencia de datos (T-01)
* **Etapa:** Implementation / Data Access
* **Herramienta / modelo:** Antigravity CLI 1.2.9 (Gemini 3.8 Flash)
* **Fecha:** 2026-09-24
* **Prompt/objetivo:** Executar el flujo de lectura de especificaciones e implementar únicamente T-01 (`load_customers` en `repository.py`).
* **Contribución de la IA:** Inspeccionó los archivos `.md`, instaló las dependencias faltantes (`fastapi`, `httpx`) mediante terminal y redactó la función de lectura de JSON.
* **Decisión del estudiante:** Se detectó que no había guardado el archivo en el primer intento y se le indicó corregir e implementar realmente el cambio.
* **Impacto:** Creación funcional de `src/repository.py`.

### Entrada 02: Lógica de búsqueda y validación (T-02)
* **Etapa:** Implementation / Core Business Logic
* **Herramienta / modelo:** Antigravity CLI 1.2.9 (Gemini 3.8 Flash)
* **Fecha:** 2026-09-24
* **Prompt/objetivo:** `1. Propose the implementation approach... 2. Implement only that task (T-02)...`
* **Contribución de la IA:** Implementó `filter_customers` en `src/logic.py` con validación de longitud de query (`len < 3`) y filtrado en minúsculas.
* **Decisión del estudiante:** Aprobado tras verificar las pruebas unitarias rápidas ejecutadas por la IA en la terminal.
* **Impacto:** Lógica de negocio completada en `src/logic.py`.

### Entrada 03: Exposición del Endpoint HTTP (T-03)
* **Etapa:** Implementation / API Layer
* **Herramienta / modelo:** Antigravity CLI 1.2.9 (Gemini 3.8 Flash)
* **Fecha:** 2026-09-24
* **Prompt/objetivo:** Avanzar a la siguiente tarea incompleta (T-03: API Endpoint).
* **Contribución de la IA:** Conectó la lógica y el repositorio dentro de `src/main.py` mediante un endpoint `GET /api/customers/search`, mapeando `ValueError` a HTTP 400.
* **Decisión del estudiante:** Aprobado al verificar la respuesta JSON adecuada ante errores y consultas válidas.
* **Impacto:** API operativa en `src/main.py`.

### Entrada 04: Pruebas Automatizadas de Integración (T-04)
* **Etapa:** Testing
* **Herramienta / modelo:** Antigravity CLI 1.2.9 (Gemini 3.8 Flash)
* **Fecha:** 2026-09-24
* **Prompt/objetivo:** Implementar la suite de pruebas en `tests/test_api.py` para cubrir los Criterios de Aceptación (AC-01, AC-02, AC-03).
* **Contribución de la IA:** Escribió los test cases utilizando `fastapi.testclient.TestClient` y ejecutó `pytest -v`.
* **Decisión del estudiante:** Aceptado tal cual al obtener la confirmación de 3/3 tests pasados.
* **Impacto:** Cobertura automatizada del 100% de los Criterios de Aceptación en `tests/test_api.py`.

### Entrada 05: Documentación de usuario final
* **Etapa:** Documentation
* **Herramienta / modelo:** Antigravity CLI 1.2.9 (Gemini 3.8 Flash)
* **Fecha:** 2026-09-24
* **Prompt/objetivo:** `como ultimo task quiero que reqalices el readme con Instalación, ejecución y pruebas`
* **Contribución de la IA:** Redactó el archivo `README.md` completo con ejemplos de instalación, guía de `uvicorn` y comandos de `pytest`.
* **Decisión del estudiante:** Aceptado.
* **Impacto:** Creación de `README.md`.