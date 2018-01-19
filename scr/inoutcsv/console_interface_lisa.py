import os
from stat import *


# ---------------------- FUNCTION -------------------------------------------------------------
def find_file(name):
    """function, which takes as an argument a filename and returns a list with all the file
    paths matching the filename"""
    path_list = []     # result list for matching file paths
    start = "C:\\"
    for root, dirs, files in os.walk(start):
        if name in files:
            path_list.append(os.path.join(root, name))
    return path_list   # returns a list with all the file paths matching


# ----------------------------------------------------------------------------------------------
test_input = True
curdir = os.path.abspath(os.path.curdir)    # path of current directory
while test_input:
    print("Current directory: ", os.path.abspath(curdir))
    print("______________________________________________________________")
    print("Files in current directory:")
    for i in range(len(os.listdir(curdir))):
        print(i, "  ", (os.listdir(curdir)[i]))
    print("______________________________________________________________")
    user_input = input("Enter the file you want to open (to terminate enter 'exit'): ")

    try:
        if user_input == "exit":
            quit()
        path = find_file(user_input)
        if len(path) != 0 and user_input not in os.listdir(curdir):
            print("The file you are searching for is not in current directory:")
            print("There is a file in ", path)
            user_confirm = input("Do you want to open this file? (Yes/No)?")
            if user_confirm == "Yes":
                print(path[0])
                test_input = False
        mode = os.stat(os.path.abspath(user_input))[ST_MODE]   # test if file or directory
        print(os.path.abspath(user_input))
        if S_ISDIR(mode):
            print("It is a directory")
            curdir = os.path.abspath(user_input)
        elif S_ISREG(mode):
            print("it is a file")
            print("path of the file ", os.path.abspath(user_input))
            test_file = os.open(user_input, os.O_RDONLY)
            print("file opened")
            os.close(test_file)
            test_input = False
        else:
            # Unknown file type, print a message
            print('Unknown file type ')
    except FileNotFoundError:  # if file/directory is requested which doesn't exist
        print("File not found")
