# PDF-Jack

## Desenvolvido para linux

## Projeto CLI para trabalhar com pdfs de maneira optmizada no linux, salvando tempo em relação a programas com interface gráfica.

## Instalação:
    1. Clone o repositório: git clone git@github.com:hugovallada/pdf-jack.git.
    2. Entre no diretório do projeto (cd pdf-jack) e execute pip install -r requirements.txt.
    3. Adicionar um alias para o executável python: alias pdf='python main.py' ou navegar até o diretório e executar manualmente(cd pdf-jack/src & python main.py).

## Utilização: 
### merge : Junta todos os arquivos pdfs em um determinado diretório, ou arquivo zip, fazendo a extração para o diretório raiz.
### ex: pdf merge /home/user/trabalhos --name trabalhos --safe --manager
#### Parâmetros da função merge:
    PATH (Obrigatório) : Passa a localização do diretório/arquivo zip.
    --name (Opcional) - Default = '' : Passa o nome do arquivo gerado, caso não passe, o arquivo se chamará merged.pdf.
    --safe (Opcional) - Default = False : Adiciona _merged ao fim do nome do arquivo, arquivos com _merged no nome, nunca são adicionados ao
     merge.
    --extract (Opcional) - Default = False : Indica se o path passado é um arquivo zip a ser descompactado.
    --extract-to (Opcional) - Default = '': Passa o diretório para onde a o conteúdo do arquivo zip deve ser extraido, caso não seja passado, o conteudo será extraido no mesmo diretório do arquivo.
    --manager (Opcional) - Default = False : Determina se o gerenciador de arquivos deve ser iniciado no diretório onde o merged foi gerado ou não.