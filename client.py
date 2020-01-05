import socket


def exe():
    host = "127.0.0.1"
    port = 5003

    s = socket.socket()
    s.connect((host, port))

    filename = input("Filename? :")
    if filename != 'Q':
        s.send(filename.encode())
        data = s.recv(1024).decode()
        if data[:11] == "FILE EXISTS":
            filesize = int(data[19:])
            message = input(
                f"File Size:{str(filesize)}Bytes. Download? (Y/N) -- ")
            if message == "Y":
                s.send('Downloading'.encode())
                f = open(f'new_{filename}', "wb")
                data = s.recv(1024)
                totalSize = len(data)
                f.write(data)
                while totalSize < filesize:
                    data = s.recv(1024)
                    totalSize += len(data)
                    f.write(data)
                    print("{0:.2f}".format((totalSize / float(filesize)) * 100) + "%")
                print("Done")
                s.close()
        else:
            print("File does not exist")
            s.close()
    s.close()


if __name__ == "__main__":
    exe()
