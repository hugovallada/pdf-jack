#! /home/hugo/Development/Python/Projects/pdf-jack/venv/bin/python

from pathlib import Path
from typing import Optional
from PyPDF2.merger import PdfFileMerger
import typer
from PyPDF2 import PdfFileMerger


app = typer.Typer()

# pdf='~/Development/Python/Projects/pdf-jack/src/./main.py'
@app.command()
def merge(path: str, name: Optional[str] = None):
    path = Path(path)
    merger = PdfFileMerger()
    for document in path.iterdir():
        if document.is_file() and document.suffix == '.pdf':
            if document.name == 'merged.pdf':
                continue
            merger.append(str(document))
    filename = 'merged' if name == None else f'{name}_merged'
    with open(f'{path}/{filename}.pdf', 'wb') as pdf:
       merger.write(pdf)
    

    
if __name__ == '__main__':
    app()