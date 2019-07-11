import tkinter as tk
import tkinter.font as tkFont
import random


class Driver:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="Are you sure you want to delete?").pack()
        self.button = tk.Button(self.master, text="Delete", command=self.recursive_delete).pack()
        self.default_font = tkFont.nametofont("TkDefaultFont")
        self.default_font.configure(size=20)

    # noinspection PyAttributeOutsideInit
    def recursive_delete(self):
        self.app = self.Stats(tk.Toplevel(self.master))

    class Stats:
        def __init__(self, master):
            with open('Delete_Strings.txt', 'r') as fin:
                self.file = fin.read()
                self.file_arr = self.file.split('\n')
                self.label = tk.Label(master, text=random.choice(self.file_arr))
                self.label.grid(columnspan=2)

            self.cont = tk.Button(master, text="Yes", command=app.recursive_delete)
            self.cont.grid(row=1, column=0)
            self.stop = tk.Button(master, text="No", command=master.quit)
            self.stop.grid(row=1, column=1)


if __name__ == '__main__':
    # STARTS THE PROGRAM
    root = tk.Tk()
    app = Driver(root)
    root.mainloop()