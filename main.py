import os
import atexit
import progressbar
from ftplib import FTP

def login():
  ftp = FTP('ftp.bmf.com.br')
  ftp.login()

  return ftp


def mkdir(folder_name):
  if not os.path.isdir(folder_name):
    os.mkdir(folder_name)


def download_file(ftp, f, folder=None):
  output_file = f'marketData/{f}'
  if folder:
    output_file = f'marketData/{folder}/{f}'
  if not os.path.isfile(output_file):
    ftp.retrbinary("RETR " + f, open(output_file, 'wb').write)


def download_folder(ftp, folder):
  is_root = '/MarketData' in folder
  ftp.cwd(folder)
  ls = ftp.nlst()
  files = [f for f in ls if '.' in f]
  
  if is_root:
    print('Baixando arquivos...')
  else:
    files = [f for f in files if not os.path.isfile(f'marketData/{folder}/{f}')]

  with progressbar.ProgressBar(max_value=len(files)) as bar:
    for i, f in enumerate(files):
      if is_root:
        download_file(ftp, f)
        bar.update(i)
      else:
        download_file(ftp, f, folder)
        bar.update(i)

  dirs = list(set(ls) - set(files))

  for folder in dirs:
    mkdir(f'marketData/{folder}/')
    print(f'Baixando arquivos da pasta marketData/{folder}')
    download_folder(ftp, folder)


def exit_handler(ftp):
  try:
    print('Finalizando script...')
    ftp.close()
  except:
    pass


def main():
  ftp = login()
  atexit.register(exit_handler, ftp)
  mkdir('marketData')
  download_folder(ftp, '/MarketData')
  exit_handler(ftp)

  
if __name__ == "__main__":
  main()
