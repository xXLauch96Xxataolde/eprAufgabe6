"""The Main Function

This module controls the procedure of the program
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
    if file_handler_obj.filename != "":   # if a file was chosen
        content = file_handler_obj.read_file()
        if content == 0:    # chosen file not found
            error_code(0)
        else:
            print(content)
            json_obj = analyzer.analyzer(content)
            parsed = json.loads(json_obj)
            print(json.dumps(parsed, indent=4, sort_keys=True,
                             ensure_ascii=False))  # encoding
    else:  # if user presses cancel button
        print("Programm wird abgebrochen")


# -------- MAIN -----------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
