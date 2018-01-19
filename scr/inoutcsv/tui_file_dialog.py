import fnmatch
import os
import main
import sys


__author__ = "5241945: Elisabeth Zeyen, 6785468: Robert Anselm Dieter am Wege"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "lisa.zeyen@outlook.com, uni.goethe.horde@gmail.com"


def dict_printer(files_dict):
    """procedure, which prints out numerated the files in a directory"""
    for k in files_dict:
        print(k, files_dict[k])


def list_dirs():
    """function, which lists the directories in current directory"""
    files_dict = {}
    i = 0
    print("**********************************")
    print("Listing all directories")
    try:
        dirs = next(os.walk('.'))[1]    # returns all the directories
    except StopIteration:               # no directory to open
        print("Can't open this directory")
        return 0

    for file in dirs:
        files_dict[i] = file            # saves files in dictionary
        i += 1

    dict_printer(files_dict)
    if len(files_dict):  # 0 is False
        print("Enter [ 0 -", len(files_dict) - 1, "] to open directory or press 'exit' to choose"
                                                  "a new command")
    else:                # no files in directory
        return 2

    while True:
        try:
            inp = input()
            # check for correct input
            if len(files_dict) != 0 and inp != "exit" and int(inp) < len(files_dict):
                filepath = str(os.getcwd()) + "\\" + files_dict[int(inp)]
                return filepath
            elif inp == "exit":
                return 1
            else:
                print("Non valid input")
        except ValueError:   # not an integer is entered as input
            print("No parsable Input. Repeat")  # yes this word exists


def list_txts():
    """function, which returns the files of type .txt of the current directory"""
    files_dict = {}
    i = 0
    print("**********************************")
    print("Listing all files")
    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.txt"):   # returns True if filename ends with .txt
            files_dict[i] = file
            i += 1

    dict_printer(files_dict)
    if len(files_dict):  # if there are files
        print("Enter [ 0 -", len(files_dict) - 1, "] to open *.txt or press 'exit' to choose a"
              " new command")
    else:
        return 2         # if there are no files

    while True:
        try:
            inp = input()
            # check for correct input
            if len(files_dict) != 0 and inp != "exit" and int(inp) < len(files_dict):
                filepath = str(os.getcwd()) + "\\" + files_dict[int(inp)]
                return filepath
            elif len(files_dict) == 0:
                print("No *.txt here")
            elif inp == "exit":
                return 1
            else:
                print("Non valid input")
        except ValueError:
            print("No parsable Input. Repeat")


def tui_main():
    """main function of the console user interface"""
    print("*************************************************************************")
    print("Current directory:")
    print(os.path.abspath(os.curdir))
    print("*************************************************************************")
    # dir up number
    print("•	 to open a list of the directories in current directory press 'dir' \n"
          "•	 to open a list of the *.txt files in current directory press 'txt' \n"
          "•	 to move one directory up press 'up' \n"
          "•	 to quit press 'exit' \n"
          " -----------------------------------------------------------------------")
    while True:
        inp = input()
        if inp == "up":     # move one directory up
            if os.path.abspath(os.curdir) != "C:\\":
                os.chdir("..")
                print((os.path.abspath(os.curdir)))
            else:
                print("You reached C:\\. There is no way up.")
        elif inp == "txt":   # show *.txt files
            file = list_txts()
            if file == 0:
                print("Error with txt")
                os.chdir("..")
            elif file == 1:
                os.path.abspath(os.curdir)
                print(os.path.abspath(os.curdir))
            elif file == 2:
                print("No *.txt files")
                os.path.abspath(os.curdir)
                print(os.path.abspath(os.curdir))
            else:
                return file
        elif inp == "dir":   # show directories
            file = list_dirs()
            if file == 0:
                print("Error with dir")
                os.chdir("..")
            elif file == 1:
                os.path.abspath(os.curdir)
            elif file == 2:
                print("No sub dirs")
                os.path.abspath(os.curdir)
            else:
                os.chdir(file)
            print(os.path.abspath(os.curdir))
        elif inp == "exit":   # to exit
            main.error_code(2)
            sys.exit()
        else:
            print("Non valid input. Repeat")
