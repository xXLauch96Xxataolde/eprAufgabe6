"""The Main Function

This module is the start of our pah_tum program. It holds the menue, the help docs and 
initializes the construction of the roots and class objects. 
"""

from file_handler import Handler
import analyzer
from textwrap import indent
import json
from idlelib.iomenu import encoding

__author__ = "1234567: Xmas Jesus"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


def error_code(n):
    if(n == 0):
        print("No such file or directory")


def main():
    file_handler_obj = Handler()
    content = file_handler_obj.read_file()
    if(content == 0):
        error_code(0)
    else:
        print(content)
        json_obj = analyzer.analyzer(content)
        parsed = json.loads(json_obj)
        print(json.dumps(parsed, indent=4, sort_keys=True,
                         ensure_ascii=False))  # encoding


if __name__ == '__main__':
    main()
