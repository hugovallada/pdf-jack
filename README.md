# PDF-Jack

## Projeto CLI para trabalhar com pdfs de maneira optmizada, salvando tempo em relação a programas com interface gráfica

## Funções do programa : 
### merge : Junta todos os arquivos pdfs em um determinado diretório
#### Args:
    PATH (Obrigatório) : Passa a localização do diretório/arquivo zip
    --name (Opcional) - Default = '' : Passa o nome do arquivo gerado, caso não passe, o arquivo se chamará merged.pdf
    --safe (Opcional) - Default = False : Adiciona _merged ao fim do nome do arquivo, arquivos com _merged no nome, nunca são adicionados ao
     merge.
    --zip (Opcional) - Default = False : Indica se o path passado é um arquivo zip a ser descompactado
    --manager (Opcional) - Default = False : Determina se o gerenciador de arquivos deve ser iniciado no diretório onde o merged foi gerado ou não