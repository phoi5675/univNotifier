import os


def deleteFileFromDirectory(absoluteLocation, fileName):
    if os.path.isfile(absoluteLocation + fileName):
        os.remove(absoluteLocation + fileName)
