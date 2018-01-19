"""The Main Function

This module controls the procedure of the program
"""

import json
import sys
from file_handler import Handler
import analyzer
import tui_file_dialog


__author__ = "5241945: Elisabeth Zeyen, 6785468: Robert Anselm Dieter am Wege"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "lisa.zeyen@outlook.com, uni.goethe.horde@gmail.com"


# ------------------FUNCTIONS----------------------------------------------------------------------
def error_code(n):
    """procedure, if there is an error with the chosen file"""
    if n == 0:
        print("No such file or directory.")
    elif n == 1:
        print("Can not decode file.")
    elif n == 2:
        print("Process aborted by User.")
    elif n == 3:
        print("LookupError: unknown encoding")


def option_tui():
    """functions, which regulates the console user interface"""
    filepath = tui_file_dialog.tui_main()
    print(filepath)
    file_handler_obj = Handler(1, filepath)
    content = file_handler_obj.read_file()
    if isinstance(content, int):   # if content is of type int turns True
        error_code(content)         # error with the chosen file
    else:
        filepath = content[1]
        content = content[0]
        # if no problem in file, a content is a tuple
        json_obj = analyzer.analyzer(content, filepath)
        parsed = json.loads(json_obj)


def option_gui():
    """function, which regulates the graphical user interface"""
    file_handler_obj = Handler()
    content = file_handler_obj.read_file()
    if isinstance(content, int):   # if content is of type int turns True
        error_code(content)        # error with the chosen file
    else:
        filepath = content[1]
        content = content[0]
        # if no problem in file, a content is a tuple
        json_obj = analyzer.analyzer(content, filepath)
        parsed = json.loads(json_obj)


def main():
    """main function"""
    while True:
        inp = input("Choose your prefered interface: \n 1 console user interface (press '1') \n"
              " 2 graphical user interface (press '2')\n --------------------------------------\n"
              "→ to leave the program enter 'exit' ")
        if inp == "1":
            option_tui()
            break
        elif inp == "2":
            option_gui()
            break
        elif inp == "exit":
            sys.exit()
        else:
            print("Non valid input")
            print("______________________________________")


# -------- MAIN ----------------------------------------------------------
if __name__ == '__main__':
    main()
