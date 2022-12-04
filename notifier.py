import os
import random
import time
import requests as requests
from dotenv import load_dotenv

from models import Clipping
from helperutils import (
    API_TOKEN_PUSHOVER,
    USER_KEY_PUSHOVER,
    KINDLE_CLIPPINGS_CSV,
    read_clippings,
)


class MessageSender:
    def __init__(self, notes: list[Clipping]):
        self.notes = notes

    def send_clipping_to_notification_service(self, clipping: Clipping) -> None:
        message = self._create_notification_message(clipping)
        print(API_TOKEN_PUSHOVER)
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
            self.send_single_message()
            time.sleep(10)

    def send_single_message(self):
        random_clipping = self._get_random_clipping(self.notes)
        self.send_clipping_to_notification_service(random_clipping)

    def _get_random_clipping(self, clippings: list[Clipping]) -> Clipping:
        return random.choice(clippings)


if __name__ == "__main__":
    load_dotenv()
    notes: list[Clipping] = read_clippings(KINDLE_CLIPPINGS_CSV)
    msender = MessageSender(notes)
    msender.start_sending()
