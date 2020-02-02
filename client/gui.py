from tkinter import *

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultText = self["text"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['text'] = self['filesize']

    def on_leave(self, e):
        self['text'] = self.defaultText

root = Tk()

root.title("Magnificent file stealing app")


for i in range(1, 10):
    listButton = HoverButton(root, text=i, width=15)
    listButton.grid(row=i, column=0, sticky=W)

root.mainloop()