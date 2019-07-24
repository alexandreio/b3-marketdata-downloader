# b3-marketdata-downloader

A B3 irá descontinuar seu servidor de FTP agora dia 31/07/2019. [link](http://www.b3.com.br/data/files/40/76/60/59/745666102F630666AC094EA8/CE%20018-2019%20-%20Prorroga%C3%A7%C3%A3o%20do%20Prazo%20de%20Desativa%C3%A7%C3%A3o%20do%20Servior%20FTP.pdf)

Esse script tem como objetivo baixar todos arquivos disponíveis até a data limite.

## Instalação

Versão do Python >= 3.7.X

O script utiliza pacotes do [pip](https://pip.pypa.io/en/stable/).Antes de executar o script é necessário rodar

```bash
pip3 install -r requirements.txt
```

## Uso

Depois das bibliotecas instaladas basta rodar o main.py

```bash
python3 main.py
```

O script está configurado para não baixar arquivos repetidos, então depois da primeira vez ele irá baixar apenas os novos arquivos.

Em caso de algum bug só abrir uma issue aqui no projeto
