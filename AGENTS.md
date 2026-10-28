# AGENTS.md

## Read First
1. REQUIREMENTS.md
2. SPEC.md
3. ARCHITECTURE.md
4. docs/REPO_MAP.md

## Sources of Truth
- Requirements live only in REQUIREMENTS.md.
- Do not change requirements merely to make tests pass.

## Standard Commands
- Install dependencies: `pip install -r requirements.txt` (or FastAPI, Uvicorn, pytest)
- Run tests: `pytest -v`
- Verify repository: `scripts/verify_repo.sh`

## Change Rules
- Keep changes scoped to the requested task (`TASK UNDER TEST.md`).
- Do not weaken existing tests.
- Do not modify secrets or generated files.

## Stop Conditions
Stop and ask for human input when requirements conflict or a destructive action is required.