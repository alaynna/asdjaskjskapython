'''
  Very simple Demo for Quest

@author: Patrick Tsang
'''
import socket
import worker
import sys
from pathlib import Path

data_folder = Path("")
file_to_open = data_folder / "a.wits"

#pushing interval 
interval = 1

#local host 
bind_ip = '127.0.0.1'

# default port number
bindPort = 7080


def main(argv):
    print("Quest Demo")
    bindPort = int(argv[0])
    interval = int(argv[1])
    file_to_open = data_folder / argv[2]
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bindPort))
    server.listen(5)
    while True:
        client_sock, address = server.accept()
        client_handler= worker.worker(client_sock,interval,file_to_open)
        client_handler.start()

if __name__ == '__main__':
    main(sys.argv[1:])