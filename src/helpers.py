from datetime import date
from datetime import datetime


def get_time():
    date_time = datetime.now()
    date_time = date_time.strftime(f"%d/%m/%Y %H:%M:%S")
    return date_time


def create_log(error):
    get_time()
    with open(f"pdf-jack.log", "a") as log:
        log.write(f"[{get_time()}] - ERROR: {error}\n")

