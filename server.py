import socket
import threading
import os


def retrieve_file(name, sock):
    print("getting file")
    
    filename = sock.recv(1024).decode()
    if os.path.isfile(filename):
        sock.send(f"FILE EXISTS : SIZE {str(os.path.getsize(filename))}".encode())
        userResponse = sock.recv(1024).decode()
        if userResponse[:11] == "Downloading":
            with open(filename, "rb") as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR".encode())
    sock.close()

def exe():
    host = "127.0.0.1"
    port = 5003

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