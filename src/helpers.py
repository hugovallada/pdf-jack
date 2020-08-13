import zipfile as zp
from pathlib import Path


def check_dir(path: Path, extract_to: str) -> None:
    zipf = zp.ZipFile(path)
    lista = zipf.namelist()
    filename = lista[0].split('/')[0]
    if extract_to == "":
        return Path.joinpath(path.parents[0], filename)
    return Path.joinpath(Path(extract_to), filename)
    