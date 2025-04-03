import tkinter as tk
from tkinter import *
import ttkbootstrap
from tkinter.messagebox import showinfo
import CrudClass as modul

root = tk.Tk()

themes = ["darkly",  "cyborg", "solar", "cosmo", "minty", "morph"]
root.title("Zene Kezelő")
ttkbootstrap.Style("darkly")

def null(index):
    print(f"{index}")

file = open("CrudData.txt", "r", encoding="utf8")
adatlist = []
for i in file:
    adatlist.append(modul.zene(i))
file.close()

class app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500")
        self.main()

    def main(self):
        for i in self.root.winfo_children():
            i.destroy()
        menubar = Menu(root)
        theme = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Theme', menu=theme)
        def setTheme(index):
            ttkbootstrap.Style(themes[index])
        for i in range(len(themes)):
            theme.add_command(label=themes[i], command=lambda index=i: setTheme(index))
        self.frame1 = Frame(self.root, width=600, height=500)
        root.config(menu=menubar)

        nevLabel = Label(
            root,
            text="Zene Kezelő",
            anchor="center",
            font=("Aerial", 13, "bold"),
        )
        nevLabel.pack(pady=5)

        gombtext = ["Hozzáad", "Átrendez", "Letöröl"]
        menuGombok = []
        for i in range(3):
            button = tk.Button(
                root,
                anchor="center",
                command=lambda index=gombtext[i]: null(index),
                width=40,
                font=("Aerial", 10, "bold"),
                text=gombtext[i],
            )
            menuGombok.append(button)
            button.pack(pady=5)

    def testpage(self):
        for i in self.root.winfo_children():
            i.destroy()
        menubar = Menu(root)
        theme = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Theme', menu=theme)
        def setTheme(index):
            ttkbootstrap.Style(themes[index])
        for i in range(len(themes)):
            theme.add_command(label=themes[i], command=lambda index=i: setTheme(index))
        self.frame2 = Frame(self.root, width=600, height=500)
        root.config(menu=menubar)
        backGomb = tk.Button(
            root,
            anchor="center",
            font=("Aerial", 10, "bold"),
            command=lambda index="Vissza": self.main(),
            width=20,
            text="Vissza",
        )
        backGomb.pack(side=BOTTOM, pady=20)

app(root)
root.mainloop()