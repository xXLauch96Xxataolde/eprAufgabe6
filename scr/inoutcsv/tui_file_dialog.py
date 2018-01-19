import fnmatch
import os
from nt import chdir
import main
import sys


def dict_printer(files_dict):
    for k in files_dict:
        print(k, files_dict[k])


def list_dirs():
    files_dict = {}
    i = 0
    print("Listing all directories")
    try:
        dirs = next(os.walk('.'))[1]
    except StopIteration:
        print("Cant open this directory")
        return(0)

    for file in dirs:
        files_dict[i] = file
        i += 1

    dict_printer(files_dict)
    if (len(files_dict)):  # 0 is False
        print("Enter [ 0 -", len(files_dict) - 1, "] to open directory")
    else:
        return(2)

    while(True):
        try:
            inp = input()
            if len(files_dict) != 0 and inp != "exit" and int(inp) < len(files_dict):
                filepath = str(os.getcwd()) + "\\" + files_dict[int(inp)]
                return(filepath)
            elif(inp == "exit"):
                return(1)
            else:
                print("Non valid input")
        except ValueError:
            print("No parsable Input. Repeat")


def list_txts():
    files_dict = {}
    i = 0
    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.txt"):
            files_dict[i] = file
            i += 1

    dict_printer(files_dict)
    if (len(files_dict)):  # 0 is False
        print("Enter [ 0 -", len(files_dict) - 1, "] to open *.txt")
    else:
        return(2)

    while(True):
        try:
            inp = input()
            if len(files_dict) != 0 and inp != "exit" and int(inp) < len(files_dict):
                filepath = str(os.getcwd()) + "\\" + files_dict[int(inp)]
                return(filepath)
            elif (len(files_dict) == False):
                print("No *.txt here")
            elif(inp == "exit"):
                return(1)
            else:
                print("Non valid input")
        except ValueError:
            print("No parsable Input. Repeat")


def tui_main():
    print(os.path.abspath(os.curdir))
    # dir up number
    print("Some explanation for the user what he or she or the preferred gender or the preferred pronouns can press")
    print("Basically an explanation about the option. which goes exactly here")
    # he/she/X can use up to go up a dir
    while(True):
        inp = input()
        if inp == "up":
            if(os.path.abspath(os.curdir) != "C:\\"):
                os.chdir("..")
                print((os.path.abspath(os.curdir)))
            else:
                print("You reached C:\\. There is no way up.")
        elif inp == "txt":
            file = list_txts()
            if (file == 0):
                print("Error with txt")
                os.chdir("..")
            elif(file == 1):
                os.path.abspath(os.curdir)
                print(os.path.abspath(os.curdir))
            elif(file == 2):
                print("No *.txt files")
                os.path.abspath(os.curdir)
                print(os.path.abspath(os.curdir))
            else:
                return(file)
        elif inp == "dir":
            file = list_dirs()
            if (file == 0):
                print("Error with dir")
                os.chdir("..")
            elif(file == 1):
                os.path.abspath(os.curdir)
            elif(file == 2):
                print("No sub dirs")
                os.path.abspath(os.curdir)
            else:
                os.chdir(file)
            print(os.path.abspath(os.curdir))
        elif(inp=="exit"):
            main.error_code(2)
            sys.exit()
        else:
            print("Non valid input. Repeat")

