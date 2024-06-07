## Sobre
Projeto responsável por fazer scrapping no site de cifra de musicas: cifraclub

## Como usar o projeto
1. Instalar as dependencias `pip install -m requirements.txt`

2. No arquivo main.py passar o link da sua banda/cantor/cantora favorito e o nome do arquivo como parametro para o objeto Scrapper.

*obs: Já deixei alguns arquivos gerados para que não precise buscar no scrap do site.*

*obs 2: Se o arquivo não existiver na raiz do projeto, o projeto então vai buscar as musicas no site via scrapping*

4. Assim que rodar, vai ser gerado um arquivo .csv que será usado pela lib pandas para criar dataframe. Nesse dataframe terá:
- title (nome da banda)
- lyric (letra da musica)
- chords (lista dos acordes usados na musica)
- difficulty (o nível de dificuldade de tocar/aprender a cifra dessa música)
