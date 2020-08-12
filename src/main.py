#! /home/hugo/Development/Python/Projects/pdf-jack/venv/bin/python

from pathlib import Path
from typing import Optional
import os
import typer
from PyPDF2 import PdfFileMerger
from helpers import create_log


app = typer.Typer()
ISSUE = "https://github.com/hugovallada/pdf-jack/issues"
LOGDIR = Path.joinpath(Path(".").home(), ".local/share/pdf-jack")


@app.command()
def merge(
    path: str,
    name: Optional[str] = "",
    safe: Optional[bool] = False,
    extract: Optional[bool] = False,
    extract_to: Optional[str] = "",
    manager: Optional[bool] = False,
) -> None:
    """
    Função de merge para juntar arquivos pdfs que estão dentro de um mesmo diretório

    Args:
        path (str): Caminho do diretório ou arquivo zip.
        name (Optional[str], optional): Nome do arquivo pdf que será gerado. Defaults to "".
        safe (Optional[bool], optional): Indica se deve acrescentar 'merged' no nome, evitando que este arquivo seja incluido em caso de um novo merge. Defaults to False.
        extract (Optional[bool], optional): Indica se é um arquivo zip a ser extraido. Defaults to False.
        extract_to (Optional[str], optional): Caminho do diretório onde deve ser extraido. Defaults to "".
        manager (Optional[bool], optional): Abrir o file manager. Defaults to False.

    Raises:
        FileNotFoundError: Se o caminho passado não existir, gera um erro para evitar que o comando unzip tente extrai-lo caso o --extract seja passado
    """
    try:
        path = Path(path)
        merger = PdfFileMerger()
        if extract:
            if not path.exists():
                raise FileNotFoundError
            if extract_to == "":
                os.chdir(path.parent)
                os.system(f"unzip {path}")
            else:
                os.chdir(extract_to)
                os.system(f"unzip {path}")
            path = (
                Path(str(path).replace(".zip", ""))
                if extract_to == ""
                else Path(f'{extract_to}/{str(path.name).replace(".zip","")}')
            )
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
    except (FileNotFoundError, NotADirectoryError) as err:
        typer.echo(
            "Não foi possível encontrar o caminho passado, verifique se não houve nenhum erro."
        )
    except Exception as err:
        if Path(LOGDIR).exists():
            os.chdir(LOGDIR)
            create_log(err)
        else:
            os.mkdir(LOGDIR)
            os.chdir(LOGDIR)
            create_log(err)

        typer.echo(
            f"Um erro fatal aconteceu. O log de erro está disponível em {Path.joinpath(LOGDIR, 'pdf-jack.log')}"
        )
        typer.echo(
            f"Se precisar de ajuda, contate o desenvolverdor em {ISSUE} e envie o log com o erro"
        )


if __name__ == "__main__":
    app()
