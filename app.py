from tkinter import Tk
from tkinter import filedialog
from http.server import HTTPServer, SimpleHTTPRequestHandler
from os import chdir
import socket
from multiprocessing.pool import ThreadPool
import time

def selectFolder():
    Tk().withdraw()
    folder_selected = filedialog.askdirectory()
    chdir(folder_selected)

def serve():
    httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    print('The server will be running at ' + socket.gethostbyname(socket.gethostname()) + ':8000/ for 2 minutes!\n')
    httpd.serve_forever()


def main():
    selectFolder()

    pool = ThreadPool(processes=1)
    pool.apply_async(serve)
    time.sleep(120)
   
    pool.terminate()
    

if __name__ == '__main__':
    main()



