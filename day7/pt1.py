class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name):
        self.name = name
        self.dirs = []
        self.files = []
        self.outer = None

root = Directory("/")
curr = root

with open("day7/input.txt", "r") as file:
    line = file.readline()
    args = line.split(" ")
    if (line.startswith("$ cd")):

    elif (line.startswith("$ ls")):

        