from utils import get_soup
from table_parser.headers import extract_table_headers

URL = "https://www.nbastuffer.com/2024-2025-nba-player-stats/"


def main():
    soup = get_soup(URL)
    headers = extract_table_headers(soup)

    print(headers)


if __name__ == "__main__":
    main()
