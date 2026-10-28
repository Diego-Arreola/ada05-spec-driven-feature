#!/usr/bin/env bash
set -euo pipefail

echo "[1/2] Running automated tests"
pytest -v

echo "[2/2] Checking repository contract"
python scripts/check_repo_contract.py

echo "VERIFY REPO: PASS"