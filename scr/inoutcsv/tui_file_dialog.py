"""Module which handles the console user interface """

import fnmatch
import os
import main
import sys


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
              " a new command")
    else:                # no files in directory
        return 2

    while True:
        try:
            inp = input()
            # check for correct input
            if inp != "exit" and int(inp) < len(files_dict):
                filepath = str(os.getcwd()) + "\\" + files_dict[int(inp)]
                return filepath
            elif inp == "exit":
                return 1
            else:
                print("Non valid input")
        except ValueError:   # not an integer is entered as input
            print("No parsable Input. Repeat")  # yes this word exists


def find_file(name):
    """function, which takes as an argument a filename and

    returns a list with all the file paths matching the filename
    """
    path_list = []     # result list for matching file paths
    start = "C:\\"     # operating system windows
    for root, dirs, files in os.walk(start):
        if name in files:
            path_list.append(os.path.join(root, name))
    return path_list   # returns a list with all the file paths matching


def search_files(find_list):
    """function, which lists up the searched files, if there a found files, it asks,

     which one to open and returns the path of the selected file
     """
    if len(find_list) == 0:    # no file found
        return 2
    else:
        print(len(find_list), "File(s) found! ")
        for i in range(len(find_list)):
            print(i, "  ", find_list[i])
    while True:
        try:
            print("Enter [ 0 - ", len(find_list) - 1, "] to open or press 'exit' to choose a"
                  " new command")
            inp = input()
            # check for correct input
            if inp == "exit":
                return 1
            elif int(inp) < len(find_list):
                return find_list[int(inp)]
            else:
                print("Non valid input")
        except ValueError:
            print("No parsable Input. Repeat")


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
            if inp != "exit" and int(inp) < len(files_dict):
                filepath = str(os.getcwd()) + "\\" + files_dict[int(inp)]
                return filepath
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
    while True:
        print(" -----------------------------------------------------------------------\n"
              " •   to open a list of the directories in current directory enter",
              '\033[1m', "'dir' \n", '\033[0m'
              "•	 to open a list of the *.txt files in current directory enter", '\033[1m', "'txt'"
              " \n", '\033[0m'
              "•	 to move one directory up enter", '\033[1m', "'up' \n", '\033[0m'
              "•	 to search for a *.txt file enter", '\033[1m', "'search' \n", '\033[0m'
              "•	 to quit enter", '\033[1m', "'exit' \n", '\033[0m'
              " -----------------------------------------------------------------------")
        inp = input()
        if inp == "up":     # move one directory up
            if os.path.abspath(os.curdir) != "C:\\":   # operating system windows
                os.chdir("..")
                print("Current directory:")
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
                print("Error with directory")
                os.chdir("..")
            elif file == 1:
                os.path.abspath(os.curdir)
            elif file == 2:
                print("No sub directories")
                os.path.abspath(os.curdir)
            else:
                os.chdir(file)
            print("Current directory:")
            print(os.path.abspath(os.curdir))

        elif inp == "search":    # to search
            while True:
                searched_file = input("Enter the name of the file you are searching for: ")
                if searched_file.endswith(".txt"):
                    find_list = find_file(searched_file)
                    file = search_files(find_list)
                    if file == 1:
                        os.path.abspath(os.curdir)
                        print(os.path.abspath(os.curdir))
                        break
                    elif file == 2:
                        print("File is not found! Enter a new command")
                        break
                    else:
                        return file
                elif searched_file == "exit":
                    break
                else:
                    print("You have to search for a *.txt file!")
                    print("Search again or enter 'exit' to give a new command")

        elif inp == "exit":   # to exit
            main.error_code(2)
            sys.exit()
        else:
            print("Non valid input. Repeat")
