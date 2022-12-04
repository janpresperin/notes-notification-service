import csv

from models import Clipping

KINDLE_CLIPPINGS_CSV = "kindle_clippings.csv"
BOOKNAME_COL = "book"
DATE_COL = "date"
CLIP_COL = "clip"
API_TOKEN_PUSHOVER = "API_TOKEN_PUSHOVER"
USER_KEY_PUSHOVER = "USER_KEY_PUSHOVER"


def read_clippings(file_path: str):
    clippings = []
    with open(file_path) as f:
        reader = csv.reader(f)
        for row in list(reader):
            clippings.append(Clipping(book=row[0], date=row[1], text=row[2]))
    return clippings
