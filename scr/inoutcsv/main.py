"""The Main Function

This module is the start of our pah_tum program. It holds the menue, the help docs and 
initializes the construction of the roots and class objects. 
"""

from file_handler import Handler
import analyzer
import json

__author__ = "1234567: Xmas Jesus"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


# ------------------FUNCTIONS----------------------------------------------------------------------
def error_code(n):
    """procedure, if the chosen file is not found"""
    if n == 0:
        print("No such file or directory")


def main():
    """main function"""
    file_handler_obj = Handler()
    if file_handler_obj.filename != "":
        content = file_handler_obj.read_file()
        if content == 0:    # chosen file not found
            error_code(0)
        else:
            print(content)
            json_obj = analyzer.analyzer(content)
            parsed = json.loads(json_obj)
            print(json.dumps(parsed, indent=4, sort_keys=True,
                             ensure_ascii=False))  # encoding
    else:
        print("Programm wird abgebrochen")


# -------- MAIN -----------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
