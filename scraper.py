from csv_writer import write_csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.nbastuffer.com/nba-stats/player/"


def extract_season_links(soup) -> list[dict]:
    """
    Extract season player-stats links from NBAstuffer.
    Returns:
        [{ "season": str, "url": str }]
    """
    results = []

    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True)
        href = a["href"]

        if "NBA Player Stats" not in text:
            continue

        if href.startswith("/"):
            href = "https://www.nbastuffer.com" + href

        results.append({
            "season": text,
            "url": href
        })

    return results


def main():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }

    response = requests.get(BASE_URL, headers=headers, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    season_links = extract_season_links(soup)

    write_csv(
        filename="season_links.csv",
        fieldnames=["season", "url"],
        rows=season_links
    )


if __name__ == "__main__":
    main()
