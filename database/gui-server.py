import socket
import threading
import os
import pickle


def retrieve_file(name, sock):
    print("getting file")
    search = sock.recv(1024).decode()
    if search == "Y":
        filename = sock.recv(1024).decode()
        if filename != "server.py":
            if os.path.isfile(filename):
                sock.send(
                    f"FILE EXISTS : SIZE {str(os.path.getsize(filename))}".encode())
                user_response = sock.recv(1024).decode()
                if user_response[:2] == "go":
                    with open(filename, "rb") as f:
                        bytes_to_send = f.read(1024)
                        sock.send(bytes_to_send)
                        while bytes_to_send != "":
                            bytes_to_send = f.read(1024)
                            sock.send(bytes_to_send)
        else:
            sock.send("ERR".encode())
    elif search == "N":
        print("sending dirlist")
        filenames = []
        with os.scandir("./") as db:
            for entry in db:
                if entry.name != "server.py":
                    filenames.append(entry.name)
        # weird pickle thing
        sock.send(pickle.dumps(filenames))
        # copy and pasted code QQ, bad duncan
        filename = sock.recv(1024).decode()
        if filename != "server.py":
            if os.path.isfile(filename):
                sock.send(
                    f"FILE EXISTS : SIZE {str(os.path.getsize(filename))}".encode())
                user_response = sock.recv(1024).decode()
                if user_response[:2] == "go":
                    with open(filename, "rb") as f:
                        bytes_to_send = f.read(1024)
                        sock.send(bytes_to_send)
                        while bytes_to_send != "":
                            bytes_to_send = f.read(1024)
                            sock.send(bytes_to_send)

    sock.close()


def exe():
    host = "127.0.0.1"
    port = 4004

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
