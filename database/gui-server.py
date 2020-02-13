import socket
import threading
import os
import pickle


def retrieve_file(name, sock):
    print("sending dirlist")
    filenames = {}
    with os.scandir("./") as db:
        for entry in db:
            size = str(os.path.getsize(entry.name))
            if entry.name != "server.py" or "gui-server.py":
                filenames.update({entry.name : size})
    sock.send(pickle.dumps(filenames))
    filename = sock.recv(1024).decode()
    print(filename)
    # if statement from non GUI server file, could be removed
    if filename != "server.py" or "gui-server.py":
        with open(filename, "rb") as f:
            bytes_to_send = f.read(1024)
            sock.send(bytes_to_send)
            while bytes_to_send != "":
                bytes_to_send = f.read(1024)
                sock.send(bytes_to_send)

    sock.close()


def exe():
    host = "127.0.0.1"
    port = 4005

    s = socket.socket()
    s.bind((host, port))

    s.listen(5)

    print("Server up")
    while True:
        c, addr = s.accept()
        print(f"connected to {str(addr)}")
        t = threading.Thread(target=retrieve_file, args=("retrThread", c))
        t.start()
    s.close()


if __name__ == "__main__":
    exe()
