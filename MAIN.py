import tkinter as tk
from tkinter import *
import ttkbootstrap

root = tk.Tk()
themes = ["darkly",  "cyborg", "solar", "cosmo", "minty", "morph"]
root.geometry("300x500")
root.title("Zene Kezelő")
ttkbootstrap.Style("darkly")

menubar = Menu(root)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Theme', menu = file)
def setTheme(index):
    ttkbootstrap.Style(themes[index])
for i in range(len(themes)):
    file.add_command(label =themes[i], command =lambda index = i: setTheme(index))


def reset():
    for child in root.winfo_children():
        child.destroy()

def null(index):
    print(f"{index}")

nevLabel = Label(
    root,
    text="Zene Kezelő",
    anchor="center",
    font=("Aerial", 13, "bold"),
)
nevLabel.pack(pady=10)

gombtext = ["Hozzáad", "Kiír", "Sorrend", "Letöröl"]
menuGombok = []
for i in range(4):
    button = tk.Button(
        root,
        anchor="center",
        command=lambda index=gombtext[i]: null(index),
        width=20,
        font=("Aerial", 10, "bold"),
        text=gombtext[i],
    )
    menuGombok.append(button)
    button.pack(pady=10)

backGomb = tk.Button(
    root,
    anchor="center",
    font=("Aerial", 10, "bold"),
    command=lambda index="Vissza": null(index),
    width=20,
    text="Vissza",
)
backGomb.pack(pady=100)

root.config(menu = menubar)
root.mainloop()