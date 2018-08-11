import sys
import random
from collections import deque

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import Frame, Label, Tk, OUTSIDE ,BOTH, W, N, E, S
else:
    from tkinter import Frame, Label, Tk, OUTSIDE, BOTH, W, N, E, S


class FullScreenWindow:

    def key_press(self, key):
        wo = Label(self.tk, text="Hello!")
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if len(self.labels) >= self.max_elements:
            label_to_remove = self.labels.pop()
            label_to_remove.destroy()

        wo.place(relx=x, rely=y)
        wo.after(self.label_timeout, wo.destroy)
        self.labels.appendleft(wo)

    def __init__(self, label_timeout, max_elements):
        self.tk = Tk()
        self.max_elements = max_elements
        self.frame = Frame(self.tk)
        self.frame.bind("<Key>", self.key_press)
        self.frame.focus_set()
        self.state = False
        self.tk.attributes("-fullscreen", True)
        self.label_timeout = label_timeout

        screen_width = self.tk.winfo_screenwidth()
        screen_height = self.tk.winfo_screenheight()
        screen_resolution = str(screen_width) + 'x' + str(screen_height)
        self.tk.geometry(screen_resolution)

        self.frame.pack()

        self.labels = deque()



