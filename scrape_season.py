from utils import get_soup
from table_parser.headers import extract_table_headers
from table_parser.rows import extract_table_rows
from csv_writer import append_csv


def scrape_season(season: str, url: str):
    """
    Scrape a single season's player stats and append to CSV.
    """
    print(f"\n[INFO] Scraping season {season}")
    soup = get_soup(url)

    headers = extract_table_headers(soup)

    # add season column to schema
    csv_headers = headers + ["season"]

    rows = extract_table_rows(
        soup=soup,
        headers=headers,
        season=season,
    )

    append_csv(
        filename="nba_player_stats_all_seasons.csv",
        fieldnames=csv_headers,
        rows=rows
    )
