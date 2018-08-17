import os

def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("Bad path!")
    with open(filename) as inFile:
        for line in inFile:
            return line



