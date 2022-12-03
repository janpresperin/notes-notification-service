from __future__ import print_function
import io
import os
import argparse

import pandas as pd

from helperutils import *


def clean_book_name(book: str) -> str:
    if book[0] == "\ufeff":
        book = book[1:]
    return book


def get_components_from_highlight(highlight: str) -> list[str]:
    return list(filter(lambda item: len(item) > 0, highlight.split("\n")))


def parse_raw_clippings_to_csv_format(
    source_file: str, encoding: str = "utf-8"
) -> None:

    if not os.path.isfile(source_file):
        raise IOError("Error: cannot find " + source_file)

    df = pd.DataFrame(columns=[BOOKNAME_COL, DATE_COL, CLIP_COL])

    with io.open(source_file, "r", encoding=encoding, errors="ignore") as f:
        highlights_str = f.read()
        highlights = highlights_str.split("==========")
        for highlight in highlights:
            lines = get_components_from_highlight(highlight)
            if len(lines) != 3:
                print("Error ON LINE: ", lines)
                continue
            (
                book,
                dateinfo,
                cliptext,
            ) = lines

            book = clean_book_name(book)

            print(book, cliptext[:50])

            df.loc[len(df), :] = [book, dateinfo, cliptext]

        df.to_csv(KINDLE_CLIPPINGS_CSV, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Transform kindle clippings into a nice CSV file"
    )
    parser.add_argument("-file_path", type=str, default="./My Clippings Example.txt")
    parser.add_argument("-encoding", type=str, default="utf-8")
    args = parser.parse_args()

    parse_raw_clippings_to_csv_format(args.file_path, args.encoding)
