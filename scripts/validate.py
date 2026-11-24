#!/usr/bin/env python3
"""Validate the core schema and every example entity against it."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "ontology" / "core.schema.json"
EXAMPLES_DIR = ROOT / "examples"


def load_json(path: Path) -> object:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def main() -> int:
    schema = load_json(SCHEMA_PATH)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        print(f"schema is invalid: {exc.message}")
        return 1

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    examples = sorted(EXAMPLES_DIR.glob("*.json"))
    if not examples:
        print("no examples found")
        return 1

    failures = 0
    for path in examples:
        data = load_json(path)
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            failures += 1
            print(f"FAIL {path.name}")
            for error in errors:
                location = "/".join(str(p) for p in error.path) or "<root>"
                print(f"  at {location}: {error.message}")
        else:
            print(f"ok   {path.name}")

    print(f"\n{len(examples) - failures}/{len(examples)} examples valid")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
