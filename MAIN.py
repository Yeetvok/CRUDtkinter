import tkinter as tk
from tkinter import *
import ttkbootstrap

root = tk.Tk()

themes = ["darkly",  "cyborg", "solar", "cosmo", "minty", "morph"]
root.title("Zene Kezelő")
ttkbootstrap.Style("darkly")

menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Theme', menu = file)
def setTheme(index):
    ttkbootstrap.Style(themes[index])
for i in range(len(themes)):
    file.add_command(label =themes[i], command =lambda index = i: setTheme(index))

class app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x500")
        self.main()

    def main(self):
        for i in self.root.winfo_children():
            i.destroy()
        theme()
        self.frame1 = Frame(self.root, width=300, height=500)
        root.config(menu = menubar)


root.config(menu = menubar)
app(root)
root.mainloop()