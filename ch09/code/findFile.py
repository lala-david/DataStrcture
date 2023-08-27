import os

def find(directory):
    for entry in os.scandir(directory):
        if entry.is_dir() and not entry.name.startswith((".", "..")):
            print("Directory:", entry.path)
        elif entry.is_file():
            print("File:", entry.path)

find(".")
