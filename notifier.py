import dataclasses
import random
import time

import pandas as pd

from helperutils import *

@dataclasses.dataclass
class Clipping():
    book: str
    date: str
    text: str


def send_clipping_to_notification_service(clipping: Clipping):
    print("Sent the record")


if __name__ == '__main__':
    df = pd.read_csv(CSVNAME)
    num_records = len(df)
    while True:
        random_number = random.randint(0, num_records)
        clipping = df.iloc[random_number]
        book, date, text = clipping[BOOKNAME_COL], clipping[DATE_COL], clipping[CLIP_COL]
        clipping = Clipping(book, date, text)
        send_clipping_to_notification_service(clipping)
        time.sleep(3600)