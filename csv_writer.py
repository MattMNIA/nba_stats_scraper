import csv
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def append_csv(filename: str, fieldnames: list[str], rows: list[dict]) -> None:
    """
    Append rows to a CSV file. Creates it if missing.
    """
    path = DATA_DIR / filename
    file_exists = path.exists()

    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerows(rows)

    print(f"[OK] Appended {len(rows)} rows → {path}")
