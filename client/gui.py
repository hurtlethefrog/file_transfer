from tkinter import *
from tkinter.ttk import *


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
