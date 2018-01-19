"""Module which handles the GUI and decodes the text document
"""


import codecs
import tkinter as tk
from tkinter.filedialog import askopenfilename

__author__ = "5241945: Elisabeth Zeyen, 6785468: Robert Anselm Dieter am Wege"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "lisa.zeyen@outlook.com, uni.goethe.horde@gmail.com"


class Handler:
    read_data = None
    fname = "Morgen_Kinder.txt"
    UTF8_fname = "UTF8_Morgen_Kinder.txt"
    filepath = ""

    def __init__(self, num=2, filepath=None):
        """Constructor

        we see some odd default values for num and filepath. This is because the tui version
        uses an instance of this class as well the gui version. because the constructor is 
        loaded anyway and loads a tkinter instance, the default values had to be put in place. 
        A tui version doesn't require a gui (like really) but should somehow transfer a filepath.
        Thats the reason for default values here.   
        """

        if (num == 1):
            self.filepath = filepath
        elif (num == 2):
            """class inisialization"""
            self.root = tk.Tk()
            self.root.attributes("-topmost", True)
            self.root.withdraw()
            self.filepath = askopenfilename()   # creates a file dialog object

    def read_file(self, filepath=None):
        """read_file

        catch lookup error with buffering 
        and return error = 3
        """
        file_encoding = " "
        # dictionary to test for different coding systems
        if (self.filepath == ""):  # checks if user aborted file dialog
            return(2)
        print("Filepath:", self.filepath)

        encode_dict = {
            codecs.decode(codecs.BOM_UTF8, "cp1252"): "UTF-8-SIG",
            codecs.decode(codecs.BOM_UTF16_LE, "cp1252"): "UTF-16",
        }
        try:
            f = open(self.filepath, "r")
            temp = f.readline()       # save the first line in an string temp
            f.close()
        except UnicodeDecodeError:
            return(1)

        for key in encode_dict:
            if temp.startswith(key):  # check for empty lines
                # determines, which encoding is used
                file_encoding = encode_dict.get(key)
                print("Codec found", encode_dict.get(
                    key), "\n")   # for testing
                break
            f.close()

        try:
            try:
                with open(self.filepath, "r", encoding=file_encoding, errors="surrogateescape",
                          buffering=1) as f:
                    # buffering=1 means line buffered, errors = 'surrogateescape' replace byte to
                    # encoding code, if error, turn back to same byte
                    self.read_data = f.read()
                f.close()
            except LookupError:
                return(3)
            return (self.read_data, self.filepath)
        except FileNotFoundError:  # if file/directory is requested which doesn't exist
            return(0)
