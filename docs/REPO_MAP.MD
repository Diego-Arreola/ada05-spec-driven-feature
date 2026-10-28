# Repository Map

## Entry Points
- `src/main.py`: FastAPI application routes and bootstrap.
- `src/logic.py`: Core search and filtering business rules.
- `src/repository.py`: Static JSON data loading layer (`src/data.json`).

## Tests
- `tests/test_api.py`: Integration test suite using FastAPI `TestClient`.

## Change Guide
If changing search behavior:
1. Check `REQUIREMENTS.md`.
2. Modify `src/logic.py`.
3. Update/add tests in `tests/test_api.py`.
4. Run `scripts/verify_repo.sh`.