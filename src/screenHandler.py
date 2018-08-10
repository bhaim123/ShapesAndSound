import sys
import random

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import Frame, Label, Tk, OUTSIDE ,BOTH, W, N, E, S
else:
    from tkinter import Frame, Label, Tk, OUTSIDE, BOTH, W, N, E, S

class FullscreenWindow:

    def keydown(self, key):
        print(key.char)
        wo = Label(self.tk, text="Hello!")
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        wo.place(relx=x, rely=y)


    def __init__(self):
        self.tk = Tk()
        self.frame = Frame(self.tk)
        self.frame.bind("<Key>", self.keydown)
        self.frame.focus_set()
        self.state = False
        self.tk.attributes("-fullscreen", True)

        screen_width = self.tk.winfo_screenwidth()
        screen_height = self.tk.winfo_screenheight()
        screen_resolution = str(screen_width) + 'x' + str(screen_height)
        self.tk.geometry(screen_resolution)

        self.frame.pack()

        testLabel=Label(self.frame,text="fofo")
        testLabel.place(bordermode=OUTSIDE, relx=0.5,rely=0.5)


