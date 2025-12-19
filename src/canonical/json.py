"""
Canonical JSON normalization.

Rules:
- UTF-8 only
- Objects: keys sorted lexicographically
- Arrays: order preserved
- No insignificant whitespace
- No trailing commas
- Numbers unchanged
- Strings unchanged
"""

import json
from typing import Any

def _canonicalize(value: Any) -> Any:
    if isinstance(value, dict):
        return {k: _canonicalize(value[k]) for k in sorted(value.keys())}
    if isinstance(value, list):
        return [_canonicalize(v) for v in value]
    return value

def canonical_json(raw: bytes) -> bytes:
    obj = json.loads(raw.decode("utf-8"))
    canon = _canonicalize(obj)
    text = json.dumps(
        canon,
        ensure_ascii=False,
        separators=(",", ":"),
    )
    return text.encode("utf-8")
