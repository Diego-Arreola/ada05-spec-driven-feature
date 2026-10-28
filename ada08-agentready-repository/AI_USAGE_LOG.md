# AI Usage Log — ADA-08

| Entrada | Etapa | Evidencia / Detalle |
| :---: | :--- | :--- |
| **1** | Auditoría Inicial (BEFORE) | Evaluación y análisis de las 8 dimensiones del repositorio heredado de ADA-05, identificando fricciones operativas y dependencias manuales (`PYTHONPATH`). |
| **2** | Ejecución BEFORE del Agente | Prueba controlada con el prompt oficial del ADA-08 aplicando `TASK_UNDER_TEST.md` (CR-01) en el repositorio no preparado. |
| **3** | Diseño de AGENTS.md y Contrato | Creación del contrato operativo en `AGENTS.md`, el mapa de navegación `docs/REPO_MAP.md` y el script de verificación `verify_repo.sh`. |
| **4** | Implementación de Guardrails | Creación de `check_repo_contract.py` para automatizar la validación de archivos críticos del repositorio de manera determinista (Punto 15). |
| **5** | Ejecución AFTER y Evaluación | Corrida del agente en el entorno optimizado. Verificación exitosa de pruebas con `pytest` y cálculo del Delta de mejora (+15 puntos en el score global). |