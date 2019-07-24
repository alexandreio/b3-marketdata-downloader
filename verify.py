#!/usr/bin/python3

import os
import time
import queue
import threading
import subprocess
import progressbar
from os import listdir
from os.path import isdir

exitFlag = 0
files_with_error = 0
upLock = threading.Lock()
queueLock = threading.Lock()
workQueue = queue.Queue()

# Classe inspirada no artigo do link abaixo:
# https://www.tutorialspoint.com/python3/python_multithreading
class myThread (threading.Thread):
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q
    def run(self):
        process_files(self.threadID, self.q)


def process_files(threadName, q):
    global exitFlag, files_with_error

    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            f = q.get()
            queueLock.release()
            if file_is_corrupted(f):
                print(f"{f} esta corrompido")
                os.remove(f)
                upLock.acquire()
                files_with_error += 1
                upLock.release()
        else:
            queueLock.release()


def file_is_corrupted(file_path):
    proc = subprocess.run(["gzip", "-v", "-t", file_path], capture_output=True)
    res = proc.stderr.splitlines()

    return len(res) > 1


def get_files_to_analyze(folder):
    abs_path = os.path.abspath(folder)
    folders = [f'{abs_path}/{d}' for d in listdir(abs_path) if isdir(f'{abs_path}/{d}')]
    
    files_to_analyze = []
    for folder in folders:
        gz_files = [f'{folder}/{f}' for f in os.listdir(folder) if '.gz' in f]
        files_to_analyze += gz_files
    
    return files_to_analyze
    


def main():
    global exitFlag, files_with_error

    threads = []
    threadID = 1

    files = get_files_to_analyze('marketData')
    print(f'Analizando {len(files)} arquivos...')
    print('Esse processo pode demorar')
    for f in files:
        workQueue.put(f)

    for _ in range(4):
        thread = myThread(threadID, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    while not workQueue.empty():
        pass

    exitFlag = 1

    for t in threads:
        t.join()
    
    if files_with_error > 0:
        print(f'No total {files_with_error} estão corrompidos e foram apagados')
        print('Rode novamente o main.py para baixar esses arquivos')
    else:
        print('Nenhum arquivo corrompido foi encontrado!')


if __name__ == "__main__":
    main()
