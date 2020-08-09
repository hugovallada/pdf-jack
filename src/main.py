#! /home/hugo/Development/Python/Projects/pdf-jack/venv/bin/python

from pathlib import Path
from typing import Optional
import os
import typer
from PyPDF2 import PdfFileMerger


app = typer.Typer()


@app.command()
def merge(path: str, name: Optional[str] = "", safe: Optional[bool] = False):
    path = Path(path)
    merger = PdfFileMerger()
    for document in path.iterdir():
        if document.is_file() and document.suffix == ".pdf":
            if document.name == "merged.pdf":
                continue
            merger.append(str(document))
    if name != "" and safe:
        name = f"{name}_merged"

    filename = "merged" if name == "" else name
    with open(f"{path}/{filename}.pdf", "wb") as pdf:
        merger.write(pdf)
        
@app.command()
def unzip_pdf(path: str, novo_path: str):
    path = Path(path)
    novo_path = Path(novo_path)
    os.chdir(novo_path)
    os.system(f"unzip {path}")
    os.chdir(str(path).replace('.zip',''))
    os.system('ls')
    
    


if __name__ == "__main__":
    app()
