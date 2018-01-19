import os, sys
from stat import *
test_input = True
while test_input:
    print("Current directory: ", os.path.abspath(os.path.curdir))
    print("______________________________________________________________")
    curdir = os.path.abspath(os.path.curdir)
    print("Files in current directory:")
    for i in range(len(os.listdir(curdir))):
        print(i, "  ", (os.listdir(curdir)[i]))
    print("______________________________________________________________")
    user_input = input("Enter the file you want to open: ")
    try:
        mode = os.stat(os.path.abspath(user_input) )[ST_MODE]
        if S_ISDIR(mode):
            print("It is a directory")
        elif S_ISREG(mode):
            print("it is a file")
            test_file = os.open(user_input, os.O_RDONLY)
            print("file opened")
            os.close(test_file)
            test_input = False
        else:
            # Unknown file type, print a message
            print('Skipping ')
    except FileNotFoundError:  # if file/directory is requested which doesn't exist
        print("File not found")