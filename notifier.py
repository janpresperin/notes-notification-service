import dataclasses
import os
import random
import time
import requests
from dotenv import load_dotenv

import pandas as pd
from pandas import DataFrame

from helperutils import *


@dataclasses.dataclass
class Clipping:
    book: str
    date: str
    text: str


class MessageSender:
    def __init__(self, notes: DataFrame):
        self.notes = notes

    def send_clipping_to_notification_service(self, clipping: Clipping) -> None:
        message = self._create_notification_message(clipping)
        r = requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": os.getenv(API_TOKEN_PUSHOVER),
                "user": os.getenv(USER_KEY_PUSHOVER),
                "message": message,
            },
        )
        print(f"Response from Pushover: {r.text}")

    def _create_notification_message(self, clipping: Clipping) -> str:
        return f"Message: {clipping.text}"

    def start_sending(self):
        while True:
            random_clipping = self._get_random_clipping(self.notes)
            self.send_clipping_to_notification_service(random_clipping)
            time.sleep(10)

    def _get_random_clipping(self, notes_dataframe: DataFrame) -> Clipping:
        random_number = random.randint(0, len(notes_dataframe))
        clipping = notes_dataframe.iloc[random_number]
        book, date, text = (
            clipping[BOOKNAME_COL],
            clipping[DATE_COL],
            clipping[CLIP_COL],
        )
        clipping = Clipping(book, date, text)
        return clipping


if __name__ == "__main__":
    load_dotenv()
    notes: DataFrame = pd.read_csv(KINDLE_CLIPPINGS_CSV)
    msender = MessageSender(notes)
    msender.start_sending()
