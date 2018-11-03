import sys
import random
from collections import deque

if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import Frame,  Tk, Canvas, BOTH
else:
    from tkinter import Frame,  Tk, Canvas, BOTH


class FullScreenWindow:

    def __init__(self, label_timeout, max_elements):
        self.count = 0
        self.colors_count = 0
        self.tk = Tk()
        self.max_elements = max_elements
        self.frame = Frame(self.tk)
        self.frame.bind("<Key>", self.key_press)
        self.frame.focus_set()
        self.state = False
        self.tk.attributes("-fullscreen", True)
        self.label_timeout = label_timeout

        self.screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.tk.winfo_screenheight()
        screen_resolution = str(self.screen_width) + 'x' + str(self.screen_height)
        self.tk.geometry(screen_resolution)
        self.canvas = Canvas(self.frame, height=self.screen_height, width=self.screen_width)
        self.canvas.pack(fill=BOTH)

        self.frame.pack()
        self.objects = deque()

    def key_press(self, key):
        self.draw_triangle()

    def draw_triangle(self):
        x1 = random.uniform(0, 1) * self.screen_width
        y1 = random.uniform(0, 1) * self.screen_height

        x2 = random.uniform(0, 1) * self.screen_width
        y2 = random.uniform(0, 1) * self.screen_height

        x3 = random.uniform(0, 1) * self.screen_width
        y3 = random.uniform(0, 1) * self.screen_height

        x4 = random.uniform(0, 1) * self.screen_width
        y4 = random.uniform(0, 1) * self.screen_height

        x5 = random.uniform(0, 1) * self.screen_width
        y5 = random.uniform(0, 1) * self.screen_height

        colors = ['black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']
        if self.colors_count % 7 == 0:
            self.colors_count = 0

        if self.count == 0:
            o = self.canvas.create_line(x1, y1, x2, y2, x3, y3, x1, y1)
            self.count = 1
        elif self.count == 1:
            o = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[self.colors_count])
            self.colors_count += 1
            self.count = 2
        elif self.count == 2:
            o = self.canvas.create_oval(x1, y1, x2, y2, fill=colors[self.colors_count])
            self.colors_count += 1
            self.count = 3
        elif self.count == 3:
            o = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, fill=colors[self.colors_count])
            self.colors_count += 1
            self.count = 0
        if len(self.objects) >= self.max_elements:
            obj_to_remove = self.objects.pop()
            self.canvas.delete(obj_to_remove)
        self.objects.appendleft(o)
        self.canvas.after(self.label_timeout,self.canvas.delete, o)
        self.frame.pack(fill=BOTH, expand=1)
