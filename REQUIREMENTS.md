# Requirements: Customer Search

## User Story
As a user,
I want to search customers by name or email,
so that I can quickly find the customer record I need.

## Functional Requirements
* **FR-01**: El sistema debe exponer un endpoint HTTP para buscar clientes enviando una cadena de texto.
* **FR-02**: El sistema debe buscar coincidencias tanto en el campo de "nombre" como en el de "correo electrónico" de los clientes.
* **FR-03**: El sistema debe soportar coincidencias parciales (substring matching) ignorando mayúsculas y minúsculas (case-insensitive).
* **FR-04**: El sistema debe retornar un arreglo de objetos JSON con los campos: `id`, `name`, y `email`.
* **FR-05**: Si no se encuentran clientes, el sistema debe retornar un código HTTP 200 con un arreglo vacío.
* **FR-06**: El sistema debe requerir un mínimo de 3 caracteres para ejecutar la búsqueda. Si es menor, debe retornar un error HTTP 400 Bad Request.

## Non-Functional Requirements
* **NFR-01**: El sistema debe ser implementado como una API HTTP local en Python 3.11+ utilizando FastAPI.
* **NFR-02**: El tiempo de respuesta de la búsqueda no debe exceder los 200ms.
* **NFR-03**: La persistencia debe manejarse mediante un archivo estático JSON local, sin bases de datos externas.

## Open Questions
* **Q-01**: ¿Se debe implementar un límite (limit/offset) en los parámetros de consulta HTTP para la paginación?

## Constraints / Assumptions
* **C-01**: Se utilizará `pytest` junto con `TestClient` de FastAPI para las pruebas automatizadas[cite: 4].