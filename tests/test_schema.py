"""Schema contract tests: valid examples pass, broken facts fail."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "ontology" / "core.schema.json").read_text(encoding="utf-8"))
EXAMPLE = json.loads((ROOT / "examples" / "lake-x.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def errors_for(data: dict) -> list:
    return list(VALIDATOR.iter_errors(data))


def test_schema_is_valid():
    Draft202012Validator.check_schema(SCHEMA)


def test_example_is_valid():
    assert errors_for(EXAMPLE) == []


def test_missing_id_fails():
    data = copy.deepcopy(EXAMPLE)
    del data["id"]
    assert errors_for(data)


def test_bad_lod_fails():
    data = copy.deepcopy(EXAMPLE)
    data["spatial"]["lod"] = "L9"
    assert errors_for(data)


def test_property_missing_unit_fails():
    data = copy.deepcopy(EXAMPLE)
    del data["properties"][0]["unit"]
    assert errors_for(data)


def test_property_missing_provenance_source_fails():
    data = copy.deepcopy(EXAMPLE)
    del data["properties"][0]["provenance"]["source"]
    assert errors_for(data)


def test_confidence_out_of_range_fails():
    data = copy.deepcopy(EXAMPLE)
    data["properties"][0]["provenance"]["confidence"] = 1.5
    assert errors_for(data)
