import tkinter as tk
from tkinter import *
from tkinter import ttk
import ttkbootstrap
from tkinter import messagebox
import CrudClass as modul

root = tk.Tk()

themes = ["darkly",  "cyborg", "solar", "cosmo", "minty", "morph"]
root.title("Zene Kezelő")
ttkbootstrap.Style("darkly")

def run(index):
    if index == 0:
        app.hozzaad(self=app(root))
    elif index == 1:
        app.atrendez(self=app(root))
    else:
        app.torol(self=app(root))

def save(adatlist):
    f = open("CrudData.txt", "w", encoding="utf8")
    for i in adatlist:
        f.write(f"{i.eloado}; {i.zenecim}; {i.hossz}\n")
    f.close()

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

        file = open("CrudData.txt", "r", encoding="utf8")
        adatlist = []
        for i in file:
            adatlist.append(modul.zene(i))
        file.close()

        nevLabel = Label(
            root,
            text="Zene Kezelő",
            anchor="center",
            font=("Aerial", 13, "bold"),
        )
        nevLabel.pack(pady=5)

        tree = ttk.Treeview(root)

        tree['columns'] = ("id", "eloado", "zenecim", "hossz")

        tree.column("#0", width=0, stretch=NO)
        tree.column("id", width=40, anchor=CENTER)
        tree.column("eloado", width=160, anchor=W)
        tree.column("zenecim", width=200, anchor=W)
        tree.column("hossz", width=70, anchor=W)

        tree.heading("#0", text="", anchor=W)
        tree.heading("id", text="ID", anchor=CENTER)
        tree.heading("eloado", text="Előadó", anchor=W)
        tree.heading("zenecim", text="Zenecím", anchor=W)
        tree.heading("hossz", text="Hossz", anchor=W)

        for i in range(len(adatlist)):
            tree.insert(parent='', index='end', iid=getint(i), text='',
                        values=(i + 1, adatlist[i].eloado, adatlist[i].zenecim, adatlist[i].hossz))

        tree.pack(pady=20)

        gombtext = ["Hozzáad", "Átrendez", "Letöröl"]
        menuGombok = []
        for i in range(3):
            button = tk.Button(
                root,
                anchor="center",
                command=lambda index=i: run(index),
                width=40,
                font=("Aerial", 10, "bold"),
                text=gombtext[i],
            )
            menuGombok.append(button)
            button.pack(pady=5)

    def hozzaad(self):
        for i in self.root.winfo_children():
            i.destroy()
        menubar = Menu(root)
        theme = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Theme', menu=theme)
        def setTheme(index):
            ttkbootstrap.Style(themes[index])
        for i in range(len(themes)):
            theme.add_command(label=themes[i], command=lambda index=i: setTheme(index))
        root.config(menu=menubar)

        file = open("CrudData.txt", "r", encoding="utf8")
        adatlist = []
        for i in file:
            adatlist.append(modul.zene(i))
        file.close()

        nevLabel = Label(
            root,
            text="Zene hozzáadása",
            anchor="center",
            font=("Aerial", 13, "bold"),
        )
        nevLabel.pack(pady=5)

        tree = ttk.Treeview(root)

        tree['columns'] = ("id", "eloado", "zenecim", "hossz")

        tree.column("#0", width=0, stretch=NO)
        tree.column("id", width=40, anchor=CENTER)
        tree.column("eloado", width=160, anchor=W)
        tree.column("zenecim", width=200, anchor=W)
        tree.column("hossz", width=70, anchor=W)

        tree.heading("#0", text="", anchor=W)
        tree.heading("id", text="ID", anchor=CENTER)
        tree.heading("eloado", text="Előadó", anchor=W)
        tree.heading("zenecim", text="Zenecím", anchor=W)
        tree.heading("hossz", text="Hossz", anchor=W)

        for i in range(len(adatlist)):
            tree.insert(parent='', index='end', iid=getint(i), text='',
                        values=(i + 1, adatlist[i].eloado, adatlist[i].zenecim, adatlist[i].hossz))

        tree.pack(pady=20)

        def validate_int(input):
            return input.isdigit() or input == ""

        vcmd = root.register(validate_int)

        frame1 = tk.Frame(root)
        text1 = Label(frame1, text="Előadó", font=("Aerial"))
        entry1 = tk.Entry(frame1, width=60)

        text1.pack(side="left")
        entry1.pack(side="left")
        frame1.pack()

        frame2 = tk.Frame(root)
        text2 = Label(frame2, text="Zenecím", font=("Aerial"))
        entry2 = tk.Entry(frame2, width=60)

        text2.pack(side="left")
        entry2.pack(side="left")
        frame2.pack()

        frame3 = tk.Frame(root)
        text3 = Label(frame3, text="Hossz", font=("Aerial"))
        entry3 = tk.Entry(frame3, width=10, validate='key', validatecommand=(vcmd, '%P'))
        text3_2 = Label(frame3, text=":", font=("Aerial"))
        entry3_2 = tk.Entry(frame3, width=10, validate='key', validatecommand=(vcmd, '%P'))

        text3.pack(side="left")
        entry3.pack(side="left")
        text3_2.pack(side="left")
        entry3_2.pack(side="left")
        frame3.pack()

        def mentesgomb(entry1, entry2, entry3, entry3_2, adatlist):
            if entry1 == "" or entry2 == "" or entry3 == "" or entry3_2 == "":
                messagebox.showerror("Hibás érték", "Nem kitöltött mezők vannak!")
                return
            elif int(entry3_2) > 59:
                messagebox.showerror("Hibás érték", "Ez az érték nem lehet több 59-nél!")
                return
            adatlist.append(modul.zene(f"{entry1}; {entry2}; {entry3}:{entry3_2}"))
            save(adatlist)
            self.hozzaad()

        mentesGomb = tk.Button(
            root,
            anchor="center",
            font=("Aerial", 10, "bold"),
            command=lambda: mentesgomb(entry1.get(), entry2.get(), str(entry3.get()), str(entry3_2.get()), adatlist),
            width=20,
            text="Mentés",
        )
        mentesGomb.pack(pady=20)

        backGomb = tk.Button(
            root,
            anchor="center",
            font=("Aerial", 10, "bold"),
            command=lambda index="Vissza": self.main(),
            width=20,
            text="Vissza",
        )
        backGomb.pack(side=BOTTOM, pady=20)

    def atrendez(self):
        for i in self.root.winfo_children():
            i.destroy()
        menubar = Menu(root)
        theme = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Theme', menu=theme)
        def setTheme(index):
            ttkbootstrap.Style(themes[index])
        for i in range(len(themes)):
            theme.add_command(label=themes[i], command=lambda index=i: setTheme(index))
        root.config(menu=menubar)

        nevLabel = Label(
            root,
            text="Zenék átrendezése",
            anchor="center",
            font=("Aerial", 13, "bold"),
        )
        nevLabel.pack(pady=5)

        file = open("CrudData.txt", "r", encoding="utf8")
        adatlist = []
        for i in file:
            adatlist.append(modul.zene(i))
        file.close()

        tree = ttk.Treeview(root)

        tree['columns'] = ("id", "eloado", "zenecim", "hossz")

        tree.column("#0", width=0, stretch=NO)
        tree.column("id", width=40, anchor=CENTER)
        tree.column("eloado", width=160, anchor=W)
        tree.column("zenecim", width=200, anchor=W)
        tree.column("hossz", width=70, anchor=W)

        tree.heading("#0", text="", anchor=W)
        tree.heading("id", text="ID", anchor=CENTER)
        tree.heading("eloado", text="Előadó", anchor=W)
        tree.heading("zenecim", text="Zenecím", anchor=W)
        tree.heading("hossz", text="Hossz", anchor=W)

        for i in range(len(adatlist)):
            tree.insert(parent='', index='end', iid=getint(i), text='', values=(i+1 , adatlist[i].eloado, adatlist[i].zenecim, adatlist[i].hossz))

        tree.pack(pady=20)

        def validate_int(input):
            return input.isdigit() or input == ""

        vcmd = root.register(validate_int)

        frame = tk.Frame(root)
        text1 = Label(frame, text="Átrendezés (ID): ", font=("Aerial"))
        entry1 = tk.Entry(frame, width=10, validate='key', validatecommand=(vcmd, '%P'))
        text2 = Label(frame, text="<-->")
        entry2 = tk.Entry(frame, width=10, validate='key', validatecommand=(vcmd, '%P'))

        text1.pack(side="left")
        entry1.pack(side="left")
        text2.pack(side="left")
        entry2.pack(side="left")
        frame.pack()

        def atrendezgomb(adatlist, entry1, entry2):
            if entry1 == "" or entry2 == "":
                messagebox.showerror("Hibás érték", "Nem kitöltött mezők vannak!")
                return
            elif int(entry1)-1 > len(adatlist)-1:
                messagebox.showerror("Hibás érték", "Az érték túl magas!")
                return
            elif int(entry2)-1 > len(adatlist)-1:
                messagebox.showerror("Hibás érték", "Az érték túl magas!")
                return
            elif int(entry1) == int(entry2):
                messagebox.showerror("Értékhiba", "A két érték nem lehet ugyanaz!")
                return
            ertek1 = adatlist[int(entry1) - 1]
            ertek2 = adatlist[int(entry2) - 1]
            adatlist[int(entry2) - 1] = ertek1
            adatlist[int(entry1) - 1] = ertek2
            save(adatlist)
            self.atrendez()

        atrendezGomb = tk.Button(
            root,
            anchor="center",
            font=("Aerial", 10, "bold"),
            command=lambda: atrendezgomb(adatlist, str(entry1.get()), str(entry2.get())),
            width=20,
            text="Átrendez",
        )
        atrendezGomb.pack(pady=20)


        backGomb = tk.Button(
            root,
            anchor="center",
            font=("Aerial", 10, "bold"),
            command=lambda index="Vissza": self.main(),
            width=20,
            text="Vissza",
        )
        backGomb.pack(side=BOTTOM, pady=20)

    def torol(self):
        for i in self.root.winfo_children():
            i.destroy()
        menubar = Menu(root)
        theme = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Theme', menu=theme)
        def setTheme(index):
            ttkbootstrap.Style(themes[index])
        for i in range(len(themes)):
            theme.add_command(label=themes[i], command=lambda index=i: setTheme(index))
        root.config(menu=menubar)

        nevLabel = Label(
            root,
            text="Zenék törlése",
            anchor="center",
            font=("Aerial", 13, "bold"),
        )
        nevLabel.pack(pady=5)

        file = open("CrudData.txt", "r", encoding="utf8")
        adatlist = []
        for i in file:
            adatlist.append(modul.zene(i))
        file.close()

        tree = ttk.Treeview(root)

        tree['columns'] = ("id", "eloado", "zenecim", "hossz")

        tree.column("#0", width=0, stretch=NO)
        tree.column("id", width=40, anchor=CENTER)
        tree.column("eloado", width=160, anchor=W)
        tree.column("zenecim", width=200, anchor=W)
        tree.column("hossz", width=70, anchor=W)

        tree.heading("#0", text="", anchor=W)
        tree.heading("id", text="ID", anchor=CENTER)
        tree.heading("eloado", text="Előadó", anchor=W)
        tree.heading("zenecim", text="Zenecím", anchor=W)
        tree.heading("hossz", text="Hossz", anchor=W)

        for i in range(len(adatlist)):
            tree.insert(parent='', index='end', iid=getint(i), text='',
                        values=(i + 1, adatlist[i].eloado, adatlist[i].zenecim, adatlist[i].hossz))

        tree.pack(pady=20)

        def torles(tree, adatlista):
            selected_items = tree.selection()
            if not selected_items:
                messagebox.showerror("Nincs kijelölve", "Jelölj ki legalább egy sort a törléshez.")
                return

            if not messagebox.askyesno("Megerősítés", "Biztos, hogy törlöd a kijelölt sort/sorokat?"):
                return

            for itemID in sorted(selected_items, reverse=True):
                index = int(itemID)
                tree.delete(itemID)
                del adatlista[index]
            save(adatlista)
            self.torol()

        torolGomb = tk.Button(
            root,
            anchor="center",
            font=("Aerial", 10, "bold"),
            command=lambda: torles(tree, adatlist),
            width=20,
            text="Elemek törlése",
        )
        torolGomb.pack(pady=20)

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
