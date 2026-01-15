import csv
from pathlib import Path
from scrape_season import scrape_season

DATA_DIR = Path(__file__).parent / "data"
SEASON_LINKS_FILE = DATA_DIR / "season_links.csv"


def load_season_links(path: Path) -> list[tuple[str, str]]:
    """
    Load season links from CSV.

    Expected CSV format:
        season,url
        2024-2025 NBA Player Stats,https://...
    """
    seasons = []

    if not path.exists():
        raise FileNotFoundError(f"Season links file not found: {path}")

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if "season" not in reader.fieldnames or "url" not in reader.fieldnames:
            raise ValueError(
                "season_links.csv must contain 'season' and 'url' columns")

        for row in reader:
            season_label = row["season"].strip()
            url = row["url"].strip()

            # normalize season label if needed
            # e.g. "2024-2025 NBA Player Stats" -> "2024-2025"
            season = season_label.split(" ")[0]

            seasons.append((season, url))

    return seasons


def main():
    print("[INFO] Loading season links...")
    seasons = load_season_links(SEASON_LINKS_FILE)

    print(f"[INFO] Found {len(seasons)} seasons")

    for idx, (season, url) in enumerate(seasons, start=1):
        print(f"\n[INFO] ({idx}/{len(seasons)}) Scraping {season}")
        try:
            scrape_season(season, url)
        except Exception as e:
            print(f"[ERROR] Failed to scrape {season}: {e}")


if __name__ == "__main__":
    main()
