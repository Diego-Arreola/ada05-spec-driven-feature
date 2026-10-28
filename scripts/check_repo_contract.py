from pathlib import Path
import sys

required = [
    "AGENTS.md",
    "README.md",
    "REQUIREMENTS.md",
    "SPEC.md",
    "ARCHITECTURE.md",
    "TASKS.md",
    "TASK_UNDER_TEST.md",
    "docs/REPO_MAP.md",
    "scripts/verify_repo.sh"
]

missing = [path for path in required if not Path(path).exists()]

if missing:
    print("REPO CONTRACT: FAIL")
    for path in missing:
        print(f"Missing: {path}")
    sys.exit(1)

print("REPO CONTRACT: PASS")
sys.exit(0)