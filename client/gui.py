from tkinter import *
from random import *

root = Tk()

root.title("Magnificent file stealing app")


for i in range(1, 10):
    num = random()
    Button(root, text=num, width=10).grid(row=i, column=0, sticky=W)

root.mainloop()