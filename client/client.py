import socket
import time
import pickle


def exe():
    host = "127.0.0.1"
    port = 4004

    s = socket.socket()
    s.connect((host, port))

    search = input("Do you know the file name you're looking for? (Y/N):")
    s.send(search.encode())

    if search == "Y":
        filename = input("Filename? :")
        s.send(filename.encode())
        data = s.recv(1024).decode()
        if data[:11] == "FILE EXISTS":
            filesize = int(data[19:])
            message = input(
                f"File Size:{str(filesize)}Bytes. Download? (Y/N) -- ")
            if message == "Y":
                s.send('go'.encode())
                f = open(f'new_{filename}', "wb")
                data = s.recv(1024)
                totalSize = len(data)
                f.write(data)
                while totalSize < filesize:
                    data = s.recv(1024)
                    totalSize += len(data)
                    f.write(data)
                    print("{0:.2f}".format(
                        (totalSize / float(filesize)) * 100) + "%")
                print("Done")
                s.close()
        else:
            print("File does not exist")
            s.close()

    elif search == "N":
        dir_list = pickle.loads(s.recv(1024))
        # comprehension not nessicary but I wanted to use one
        print("Here is a file list to choose from:")
        time.sleep(1)
        [print(entry) for entry in dir_list]
        filename = input("Type the file name as displayed: ")
        s.send(filename.encode())
        data = s.recv(1024).decode()
        if data[:11] == "FILE EXISTS":
            filesize = int(data[19:])
            message = input(
                f"File Size:{str(filesize)}Bytes. Download? (Y/N) -- ")
            if message == "Y":
                s.send('go'.encode())
                f = open(f'new_{filename}', "wb")
                data = s.recv(1024)
                totalSize = len(data)
                f.write(data)
                while totalSize < filesize:
                    data = s.recv(1024)
                    totalSize += len(data)
                    f.write(data)
                    print("{0:.2f}".format(
                        (totalSize / float(filesize)) * 100) + "%")
                print("Done")
                s.close()

    s.close()


if __name__ == "__main__":
    exe()
