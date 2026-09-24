# Agent Report

## Agent / Version
Antigravity CLI 1.2.9 (Gemini 3.8 Flash - High)

## Initial Context
El proyecto inició con la estructura base para una API REST con FastAPI. Los archivos `repository.py`, `logic.py`, `main.py` y `test_api.py` contenían únicamente estructuras base (`pass`) para ser completadas paso a paso por la IA según la especificación.

## Task Sequence

### T-01 Data loading
* **What the agent did:** Implementó la función `load_customers()` en `src/repository.py` para leer y parsear el archivo `src/data.json` con codificación UTF-8.
* **Human review:** El estudiante confirmó la implementación y solicitó avanzar paso a paso respetando la propuesta previa.
* **Tests:** Verificación directa con Python CLI y ejecución inicial con `pytest`.

### T-02 Search and Validation logic
* **What the agent did:** Implementó `filter_customers()` en `src/logic.py`, agregando validación de longitud mínima (mínimo 3 caracteres, lanzando `ValueError`) y filtrado insensible a mayúsculas sobre los campos `name` y `email`.
* **Human review:** Validado correctamente por el usuario.
* **Tests:** Verificación de lógica unitaria en terminal y `pytest` (3/3 stubs pasando/listos).

### T-03 API Endpoint
* **What the agent did:** Implementó el endpoint `GET /api/customers/search` en `src/main.py`, orquestando la carga de datos, captura de `q`, captura de `ValueError` para responder HTTP 400 Bad Request, y manejo de excepciones de lectura con HTTP 500.
* **Human review:** Aprobado para pasar a la suite de pruebas automatizadas.
* **Tests:** Verificación manual vía `TestClient` devolviendo códigos HTTP 200 y 400 esperados.

### T-04 Automated Tests
* **What the agent did:** Completó `tests/test_api.py` con `TestClient` para validar los tres Criterios de Aceptación: `test_search_validation_error` (AC-01), `test_search_success_match` (AC-02) y `test_search_no_results` (AC-03).
* **Human review:** Aprobado tras verificar que todas las pruebas pasaron.
* **Tests:** `pytest -v` ejecutado exitosamente (3/3 PASSED).

### Extra Task: README Documentation
* **What the agent did:** Redactó el archivo `README.md` incluyendo requisitos previa instalación, guía de instalación de dependencias, comandos de ejecución con `uvicorn`, ejemplos con `curl` y ejecución de pruebas con `pytest`.
* **Human review:** Aprobado y verificado.
* **Tests:** `pytest` ejecutado tras la actualización documental (3/3 PASSED).

## Problems Encountered
* En la ejecución inicial, la máquina local no contaba con las librerías `fastapi` y `httpx` instaladas en el entorno global de Python, lo que generaba errores de importación al ejecutar `pytest`. El agente ejecutó automáticamente `pip install fastapi httpx` para corregir la falta de entorno virtual activo.
* En el primer turno, el agente asumió la tarea sin persisitir adecuadamente los cambios en el archivo físico antes del reporte, lo cual fue señalado por el estudiante y corregido de inmediato.

## Human Interventions
* Prompts del estudiante para forzar el flujo Spec-Driven: el usuario recordó repetidamente el protocolo de 7 pasos (Inspeccionar -> Identificar incompleta -> Proponer enfoque -> Implementar SOLO esa tarea -> Probar -> Reportar -> Siguiente tarea).

## Requirement / Specification Changes
* N/A. No se modificó `REQUIREMENTS.md` ni `SPEC.md`.

## Final Verification
* `pytest -v` ejecutado en PowerShell enviando `PYTHONPATH="."`: 3 pruebas superadas al 100%.

## Lessons Learned
* El enfoque Spec-Driven asistido por CLI (Antigravity) garantiza que el código mantenga un diseño modular y desacoplado (Router -> Logic -> Repository).
* Mantener reglas de intervención paso a paso evita que los agentes generen todo el código de un solo intento sin la supervisión adecuada.