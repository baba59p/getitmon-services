"""Small offline CSV structure-check demonstration, not an import guarantee."""
import csv
import io
import json
from pathlib import Path
import sys


def check(text):
    errors = []
    rows = 0
    try:
        records = csv.reader(io.StringIO(text, newline=""), strict=True)
        header = next(records, None)
        if not header:
            errors.append({"code": "missing_header"})
        else:
            if len(set(header)) != len(header):
                errors.append({"code": "duplicate_header"})
            for number, row in enumerate(records, 2):
                rows += 1
                if len(row) != len(header):
                    errors.append({"code": "row_width", "record": number})
    except csv.Error:
        errors.append({"code": "parse_error"})
    return {"valid": not errors, "rows": rows, "errors": errors}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_csv.py input.csv", file=sys.stderr)
        raise SystemExit(2)
    try:
        result = check(Path(sys.argv[1]).read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"valid": False, "error": type(exc).__name__}))
        raise SystemExit(2)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["valid"] else 1)
