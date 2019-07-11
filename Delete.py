import tkinter as tk
import tkinter.font as tkFont
import random


class Driver:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="Are you sure you want to delete?").pack()
        self.button = tk.Button(self.master, text="Delete", command=self.recursive_delete).pack()
        self.default_font = tkFont.nametofont("TkDefaultFont")
        self.default_font.configure(size=18)

    # noinspection PyAttributeOutsideInit
    def recursive_delete(self):
        self.app = self.NewWindow(tk.Toplevel(self.master))

    class NewWindow:
        def __init__(self, master):
            self.master = master
            with open('Delete_Strings.txt', 'r') as fin:
                self.file = fin.read()
                self.file_arr = self.file.split('\n')
                self.label = tk.Label(master, text=random.choice(self.file_arr))
                self.label.grid(columnspan=2)

            self.cont = tk.Button(master, text="Yes", command=app.recursive_delete)
            self.cont.grid(row=1, column=0)
            self.stop = tk.Button(master, text="No", command=self.quit)
            self.stop.grid(row=1, column=1)

        def quit(self):
            self.app = self.QuitWindow(tk.Toplevel(self.master))

        class QuitWindow:
            def __init__(self, master):
                self.label = tk.Label(master, text="Oh ok")
                self.label.after(2000, master.quit)
                self.label.pack()


if __name__ == '__main__':
    # STARTS THE PROGRAM
    root = tk.Tk()
    app = Driver(root)
    root.mainloop()