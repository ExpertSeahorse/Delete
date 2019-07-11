import tkinter as tk
import tkinter.font as tkFont
import random


class Driver:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(self.master, text="Download mor RAM")
        self.label.bind("<Enter>", self.spam_popup)
        self.label.pack()
        self.default_font = tkFont.nametofont("TkDefaultFont")
        self.default_font.configure(size=18)

    # noinspection PyAttributeOutsideInit
    def spam_popup(self, event=None):
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        self.app = self.Spam(tk.Toplevel(self.master).geometry("+%d+%d" % (x, y)))

    class Spam:
        def __init__(self, master):
            self.label = tk.Label(master, text="Download mor RAM")
            self.label.pack()
            app.spam_popup()


if __name__ == '__main__':
    # STARTS THE PROGRAM
    root = tk.Tk()
    app = Driver(root)
    root.mainloop()
