#!/usr/bin/env python3.7
"""Usage: shapes_and_sound.py [ -h | -help ]

-h --help   A basic child game sowing a shape on every keyboard click.

"""

from lib.docopt import docopt
from src.screenHandler import FullscreenWindow

docopt(__doc__)

if __name__ == '__main__':

    w = FullscreenWindow()
    w.tk.mainloop()

