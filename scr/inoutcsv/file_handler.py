"""Docstrings
"""

import io
import codecs

__author__ = "1234567: Xmas Jesus"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


class Handler():
    read_data = 0
    read_size = 0
    fname = "Morgen_Kinder.txt"
    UTF8_fname = "UTF8_Morgen_Kinder.txt"
    
    
    def __init__(self):
        pass
    
    def test(self):
        a = codecs.open(self.fname, mode='r', encoding="Ascii", errors='strict', buffering=1)
        b = codecs.open(self.UTF8_fname, mode='r', encoding=None, errors='strict', buffering=1)
        c = codecs.BOM_UTF16
        d = codecs.BOM_UTF16_BE
        print(codecs.decode(d, "cp1252"))

    def read_file(self):
        self.test()
        try:
            fname = "Morgen_Kinder.txt"
            with open(self.fname, "r", encoding="UTF-16", errors="surrogateescape") as f:
                self.read_data = f.read()
            f.closed
            return(self.read_data)
        except FileNotFoundError:
            return(0)
