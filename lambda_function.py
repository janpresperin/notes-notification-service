from models import Clipping
from helperutils import KINDLE_CLIPPINGS_CSV, read_clippings
from notifier import MessageSender


def lambda_handler(event, context):
    # load_dotenv()
    notes: list[Clipping] = read_clippings(KINDLE_CLIPPINGS_CSV)
    msender = MessageSender(notes)
    msender.send_single_message()


if __name__ == "__main__":
    lambda_handler(1, 1)
