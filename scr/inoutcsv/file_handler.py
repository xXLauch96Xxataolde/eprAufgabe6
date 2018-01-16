"""Module which handles the GUI and decodes the text document
"""


import codecs
import tkinter as tk
from tkinter.filedialog import askopenfilename

__author__ = "1234567: Xmas Jesus"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


class Handler:
    read_data = None
    fname = "Morgen_Kinder.txt"
    UTF8_fname = "UTF8_Morgen_Kinder.txt"
    filename = ""

    def __init__(self):
        """class inisialization"""
        self.root = tk.Tk()
        self.root.withdraw()
        self.filename = askopenfilename()   # creates a file dialog object
        if self.filename == "":
            print("No file chosen")
        else:
            print("filename:", self.filename)
            self.read_file()
    
    def read_file(self):
        file_encoding = " "
        test_file = self.filename
        # dictionnary to test for different coding systems
        encode_dict = {
            codecs.decode(codecs.BOM_UTF8, "cp1252"): "UTF-8-SIG",
            codecs.decode(codecs.BOM_UTF16_LE, "cp1252"): "UTF-16",
        }

        f = open(test_file, "r")
        temp = f.readline()       # save the first line in an string temp
        f.close()

        for key in encode_dict:
            if temp.startswith(key):  # check for empty lines
                file_encoding = encode_dict.get(key)  # determines, which encoding is used
                print("Codec found", encode_dict.get(key), "\n")   # for testing
                break
            f.close()

        try:
            with open(test_file, "r", encoding=file_encoding, errors="surrogateescape",
                      buffering=1) as f:
                # buffering=1 means line buffered, errors = 'surrogateescape' replace byte to
                # encoding code, if error, turn back to same byte
                self.read_data = f.read()
            f.close()
            return self.read_data
        except FileNotFoundError:  # if file/directory is requested which doesn't exist
            return 0
