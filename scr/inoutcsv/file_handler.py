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
    fname = "Morgen_Kinder.txt"
    UTF8_fname = "UTF8_Morgen_Kinder.txt"

    def __init__(self):
        pass

    def read_file(self):
        test_file = self.UTF8_fname
        bom_dict = {
            codecs.decode(codecs.BOM_UTF8, "cp1252"): "UTF-8-SIG",
            codecs.decode(codecs.BOM_UTF16_LE, "cp1252"): "UTF-16",
        }

        f = open(test_file, "r")
        temp = f.readline()
        f.closed

        for key in bom_dict:
            if (temp.startswith(key)):  # check for empty lines
                file_encoding = bom_dict.get(key)
                print("Codec found", bom_dict.get(key), "\n")
                break
            f.closed

        try:
            with open(test_file, "r", encoding=file_encoding, errors="surrogateescape", buffering=1) as f:
                self.read_data = f.read()
            f.closed
            return(self.read_data)
        except FileNotFoundError:
            return(0)
