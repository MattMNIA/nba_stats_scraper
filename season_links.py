from utils import get_soup
from csv_writer import write_csv

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
    soup = get_soup(BASE_URL)
    season_links = extract_season_links(soup)

    write_csv(
        filename="season_links.csv",
        fieldnames=["season", "url"],
        rows=season_links
    )


if __name__ == "__main__":
    main()
