"""The Main Function

This module is the start of our pah_tum program. It holds the menue, the help docs and 
initializes the construction of the roots and class objects. 
"""

from file_handler import Handler

__author__ = "1234567: Xmas Jesus"
__copyright__ = "Copyright 2017/2018 - EPR-Goethe-Uni"
__credits__ = ""
__email__ = "uni.goethe.horde@gmail.com"


def error_code(n):
    if(n == 0):
        print("No such file or directory")


def main():
    file_handler_obj = Handler()
    if(file_handler_obj.read_file == 0):
        error_code(0)
    else:
        content = file_handler_obj.read_file()
        # print(content)


if __name__ == '__main__':
    main()
