import os

def find(directory, indent=""):

    for entry in os.scandir(directory):
        if entry.is_dir() and not entry.name.startswith((".", "..")):
            print(indent + "Directory:", entry.path)
            find(entry.path, indent + "  ") 

        elif entry.is_file():
            print(indent + "File:", entry.path)


find(".")
