import socket
import threading
import os


def retrieve_file(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send(f"FILE EXISTS : SIZE {str(os.path.getsize(filename))}")
        userResponse = sock.recv(1024)
        if userResponse[:2] == "OK":
            with open(filename, "rb") as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR")
    sock.close()
