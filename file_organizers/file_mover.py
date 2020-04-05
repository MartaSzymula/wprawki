"""This program moves is intended to move duplicated files from it\'s current location to a new one, but can also be a simple file
mover
"""
import os
import shutil



def move_duplicate(sourceFolder, destinationFolder, duplicate_indicator):

    for folderName, subfolders, filenames in os.walk(sourceFolder):

        for filename in filenames:
            if duplicate_indicator in filename:
                print(f"I\'m movng file: {filename} from folder: {folderName} to folder: {destinationFolder}")
                shutil.move(f"{folderName}/{filename}", destinationFolder)


if __name__ == '__main__':

    sourceFolder = 'C:/Users/Ja/Desktop/src'
    destinationFolder = 'C:/Users/Ja/Desktop/dest'
    print("Please input duplicate indicator (i.e. copy, (1), kopia)")
    duplicate_indicator = input()

    move_duplicate(sourceFolder, destinationFolder, duplicate_indicator)
