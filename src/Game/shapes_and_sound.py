#!/usr/bin/env python3.7
"""Usage: shapes_and_sound.py [ -h | -help ]

-h --help   A basic child game sowing a shape on every keyboard click.

"""

from lib.docopt import docopt
from src.Game.screen_handler import FullScreenWindow

docopt(__doc__)

if __name__ == '__main__':
    label_timeout = 10000
    max_elements = 10
    w = FullScreenWindow(label_timeout, max_elements)
    w.tk.mainloop()

