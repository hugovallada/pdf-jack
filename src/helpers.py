from datetime import date
from datetime import datetime
import zipfile as zp
from pathlib import Path


def get_time():
    date_time = datetime.now()
    date_time = date_time.strftime(f"%d/%m/%Y %H:%M:%S")
    return date_time


def create_log(error):
    get_time()
    with open(f"pdf-jack.log", "a") as log:
        log.write(f"[{get_time()}] - ERROR: {error}\n")


def check_dir(path: Path, extract_to: str) -> Path:
    zipf = zp.ZipFile(path)
    lista = zipf.namelist()
    filename = lista[0].split('/')[0]
    if extract_to == "":
        return Path.joinpath(path.parents[0], filename)
    return Path.joinpath(Path(extract_to), filename)
