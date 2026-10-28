# Task Under Test
Change ID: CR-01

## Goal
Enhance the search query handling in `src/logic.py` to automatically trim leading and trailing whitespace from the query string `q` before filtering customers, ensuring robust substring matching for inputs with accidental spaces.

## Requirements Covered
- FR-03 (El sistema debe soportar coincidencias parciales (substring matching) ignorando mayúsculas y minúsculas (case-insensitive).)

## Verification
Run `pytest -v` and ensure that a test validating search queries with surrounding spaces successfully returns matching records based on FR-03.

## Constraints
- Use REQUIREMENTS.md and SPEC.md as the source of truth.
- Keep changes scoped to this task.
- Do not redefine requirements in this file.