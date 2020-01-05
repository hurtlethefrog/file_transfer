import socket


def exe():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = input("Filename? :")
    if filename != 'Q':
        s.send(filename)
        data = s.recv(1024)
        if data[:11] == "FILE EXISTS":
            filesize = data[19:]
            message = input(
                f"File Size:{str(filesize)}Bytes. Download? (Y/N) -- ")
            if message == "Y":
                s.send('Downloading')
                f = open(f'new_{filename}wb')
                data = s.recv(1024)
                totalSize = len(data)
                f.write(data)
                while totalSize < filesize:
                    data = s.recv(1024)
                    totalSize = + len(data)
                    f.write(data)
                    print(f"{(totalSize/float(filesize))*100}%")
                print("Done")
        else:
            print("File does not exist")
    s.close()


if __name__ == "__Main__":
    exe()
