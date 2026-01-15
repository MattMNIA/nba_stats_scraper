from bs4 import BeautifulSoup
import re


def normalize_column_name(name: str) -> str:
    """
    Normalize column names for CSV / DB usage.
    """
    name = name.strip().lower()
    name = name.replace("%", "_pct")
    name = re.sub(r"[^\w]+", "_", name)
    return name.strip("_")


def extract_table_headers(soup: BeautifulSoup) -> list[str]:
    """
    Extract column headers from <tr class="row-1">.
    This is the authoritative DataTables header row.
    """
    header_row = soup.find("tr", class_="row-1")

    if not header_row:
        raise ValueError("Header row <tr class='row-1'> not found")

    headers = []

    for th in header_row.find_all("th", recursive=False):
        title_span = th.select_one(".dt-column-title")
        raw_name = th.get_text(strip=True)
        if raw_name:
            headers.append(normalize_column_name(raw_name))
            continue

        if title_span:
            raw_name = title_span.get_text(strip=True)
            headers.append(normalize_column_name(raw_name))

    if not headers:
        raise ValueError("No column titles found in header row")

    return headers
