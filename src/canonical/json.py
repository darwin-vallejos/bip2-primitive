"""
Canonical JSON structural ordering.

Rules:
- Objects: keys sorted lexicographically
- Arrays: order preserved
- Values unchanged
"""

import json
from typing import Any


def _canonicalize(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _canonicalize(value[key])
            for key in sorted(value.keys())
        }

    if isinstance(value, list):
        return [_canonicalize(item) for item in value]

    return value


def canonicalize_json(raw: bytes) -> bytes:
    data = json.loads(raw.decode("utf-8"))
    canonical = _canonicalize(data)

    return json.dumps(
        canonical,
        separators=(",", ":"),
        ensure_ascii=False
    ).encode("utf-8") + b"\n"
