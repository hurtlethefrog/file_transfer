from tkinter import *
from tkinter.ttk import *

import socket
import time
import pickle


class HoverButton(Button):
    def __init__(self, master, filesize, filename, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultText = filename
        self.filesize = filesize
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['text'] = self.filesize

    def on_leave(self, e):
        self['text'] = self.defaultText

# ########################### #


root = Tk()
root.geometry('600x600')

root.title("Magnificent file stealing app")

for i in range(1, 10):
    listButton = HoverButton(root, text=i, width=15, filesize=f'filesize:{i}', filename=i)
    listButton.grid(row=i, column=0, sticky=W)

style = Style()

style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'),
                foreground='red')

btn1 = Button(root, text='exit',
              style='W.TButton',
              command=root.destroy)
btn1.grid(row=0, column=6)

root.mainloop()

# ######################################## #


def exe():
    host = "127.0.0.1"
    port = 4004

    s = socket.socket()
    s.connect((host, port))

    # search = input("Do you know the file name you're looking for? (Y/N):")
    # s.send(search.encode())

    # if search.upper() == "Y":
    #     filename = input("Filename?(case sensitive:")
    #     s.send(filename.encode())
    #     data = s.recv(1024).decode()
    #     if data[:11] == "FILE EXISTS":
    #         filesize = int(data[19:])
    #         message = input(
    #             f"File Size:{str(filesize)}Bytes. Download? (Y/N) -- ")
    #         if message.upper() == "Y":
    #             s.send('go'.encode())
    #             f = open(f'new_{filename}', "wb")
    #             data = s.recv(1024)
    #             totalSize = len(data)
    #             f.write(data)
    #             while totalSize < filesize:
    #                 data = s.recv(1024)
    #                 totalSize += len(data)
    #                 f.write(data)
    #                 print("{0:.2f}".format(
    #                     (totalSize / float(filesize)) * 100) + "%")
    #             print("Done")
    #             s.close()
    #         else:
    #             s.close()
    #     else:
    #         print("File does not exist")
    #         s.close()

    elif search.upper() == "N":
        dir_list = pickle.loads(s.recv(1024))
        # comprehension not necessary but I wanted to use one
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
            if message.upper() == "Y":
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
                s.close()
    s.close()


if __name__ == "__main__":
    exe()
