import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def write_csv(filename: str, fieldnames: list[str], rows: list[dict]) -> None:
    """
    Write a list of dictionaries to a CSV file in ./data.
    Overwrites existing file.
    """
    path = DATA_DIR / filename

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[OK] Wrote {len(rows)} rows → {path}")
