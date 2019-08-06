# b3-marketdata-downloader

Esse script tem como objetivo baixar todos arquivos disponíveis até a data limite no FTP da B3.

## Instalação

Versão do Python >= 3.7.X

O script utiliza pacotes do [pip](https://pip.pypa.io/en/stable/). Antes de executar o script é necessário rodar

```bash
pip3 install -r requirements.txt
```

## Uso

Depois das bibliotecas instaladas basta rodar o main.py

```bash
python3 main.py
```

O arquivo ```verify.py``` procura e apaga arquivos que se corromperam durante o download.

O script está configurado para não baixar arquivos repetidos, então depois da primeira vez ele irá baixar apenas os novos arquivos.

Em caso de algum bug só abrir uma issue aqui no projeto
