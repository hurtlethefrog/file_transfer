from tkinter import *
from tkinter.ttk import *

import socket
import time
import pickle


class HoverButton(Button):
    def __init__(self, master, filesize, filename, socket, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultText = filename
        self.filename = filename
        self.filesize = filesize
        self.s = socket
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.send_file)

    def send_file(self, e):
        print(self.filename)
        print(self.s)
        self.s.send(self.filename.encode())
        f = open(f'new_{self.filename}', "wb")
        data = self.s.recv(1024)
        totalSize = len(data)
        f.write(data)
        while totalSize < int(self.filesize):
            data = self.s.recv(1024)
            totalSize += len(data)
            f.write(data)
            print("{0:.2f}".format(
            (totalSize / float(self.filesize)) * 100) + "%")
        print("Done")
        self.s.close()

    def on_enter(self, e):
        self['text'] = f"Filesize: {self.filesize} Bytes"

    def on_leave(self, e):
        self['text'] = self.defaultText

def exe():
    host = "127.0.0.1"
    port = 4005

    s = socket.socket()
    s.connect((host, port))

    root = Tk()
    root.geometry('600x600')

    root.title("Magnificent file stealing app")


    dir_list = pickle.loads(s.recv(1024))
    # comprehension not necessary but I wanted to use one
    print("Here is a file list to choose from:")
    # create buttons with dict pickle from server

    for i, (k, v) in enumerate(dir_list.items()):
        listButton = HoverButton(root, text=k, width=40, filesize=v, filename=k, socket=s)
        listButton.grid(row=i, column=0, sticky=W)


    root.mainloop()
    
    s.close()


if __name__ == "__main__":
    exe()
