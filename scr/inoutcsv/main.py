"""The Main Function

This module controls the procedure of the program
"""

from file_handler import Handler
import analyzer
import json
import tui_file_dialog
import sys

__author__ = "1234567: Xmas Jesus"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


# ------------------FUNCTIONS----------------------------------------------------------------------
def error_code(n):
    """procedure, if the chosen file is not found"""
    if (n == 0):
        print("No such file or directory.")
    elif (n == 1):
        print("Can not decode file.")
    elif (n == 2):
        print("Process aborted by User.")
    elif (n == 3):
        print("LookupError: unknown encoding")


def option_tui():
    filepath = tui_file_dialog.tui_main()
    print(filepath)
    file_handler_obj = Handler(1, filepath)
    content = file_handler_obj.read_file()
    if isinstance(content, int):
        error_code(content)
    else:
        filepath = content[1]
        content = content[0]
        # if no problem in file, a content is a tuple
        json_obj = analyzer.analyzer(content, filepath)
        parsed = json.loads(json_obj)


def option_gui(path=None):
    file_handler_obj = Handler()
    content = file_handler_obj.read_file()
    if isinstance(content, int):
        error_code(content)
    else:
        filepath = content[1]
        content = content[0]
        # if no problem in file, a content is a tuple
        json_obj = analyzer.analyzer(content, filepath)
        parsed = json.loads(json_obj)


def main():
    """main function"""
    while(True):
        print("Some menu nonsense with the options")
        inp = input()
        if (inp == "1"):
            option_tui()
            break
        elif(inp == "2"):
            option_gui()
            break
        elif (inp == "exit"):
            sys.exit()
        else:
            print("Non valid Input")

 # Delete ''' for json printing
'''        print(json.dumps(parsed, indent=4, sort_keys=True,
                         ensure_ascii=False))  # encoding FOR TESTING
'''

# -------- MAIN ----------------------------------------------------------
if __name__ == '__main__':
    main()
