#! /home/hugo/Development/Python/Projects/pdf-jack/venv/bin/python

from pathlib import Path
from typing import Optional
import os
import typer
from PyPDF2 import PdfFileMerger


app = typer.Typer()


@app.command()
def merge(
    path: str,
    name: Optional[str] = "",
    safe: Optional[bool] = False,
    zip: Optional[bool] = False,
    manager: Optional[bool] = False,
):
    path = Path(path)
    merger = PdfFileMerger()
    if zip:
        os.chdir(path.parent)
        os.system(f"unzip {path}")
    path = Path(str(path).replace(".zip", ""))
    for document in path.iterdir():
        if document.is_file() and document.suffix == ".pdf":
            if "merged" in document.name:
                continue
            merger.append(str(document))
    if name != "" and safe:
        name = f"{name}_merged"
    filename = "merged" if name == "" else name
    with open(f"{path}/{filename}.pdf", "wb") as pdf:
        merger.write(pdf)

    if manager:
        os.chdir(path)
        os.system("xdg-open . &")


if __name__ == "__main__":
    app()
