"""This program takes
"""
import os
from PIL.ExifTags import TAGS
from PIL import Image
import shutil

"""Extracting date based on https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3
"""

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()


def enumeration(number):

    if number <10:
        photo_num = "DSC_000" + str(number)

    elif number in range(9, 99):
        photo_num = "DSC_00" + str(number)

    elif number in range(100, 999):
        photo_num = "DSC_0" + str(number)

    else:
        photo_num = "DSC_" + str(number)

    return photo_num


def get_date(sourceFolder, destinationFolder):

    photo_list = []
    number = ""

    for folderName, subfolders, filenames in os.walk(sourceFolder):

        for filename in filenames:
            # print(filename)
            if filename.split('.')[-1].lower() == 'jpg':
                try:
                    exif = get_exif(f"{folderName}\\{filename}")[36867]
                    year = exif[0:4]
                    month = exif[5:7]
                    day = exif[8:10]

                except :
                    print("Exif didn't work for:" + filename)
                    year = '1970'
                    month = '01'
                    day = '01'


                # print(f"{year}-{month}-{day}")
                date = f"{year}-{month}-{day}"

                # os.mkdir(f"{destinationFolder}/{date}")

                photo_list.append(filename)
                # print(photo_list)
                number = len(photo_list)
                new_photo_name = enumeration(number)
                print(f"I\'m renaming file: {filename} to {new_photo_name}.jpg and moving to foler {date}")

                # shutil.move(f"{folderName}/{filename}", f"{destinationFolder}/{date}/{new_photo_name}")


if __name__ == '__main__':

    sourceFolder = 'C:/Users/Ja/Desktop/test-JP'
    destinationFolder = 'C:/Users/Ja/Desktop/dest-JP'
    # print("Please input duplicate indicator (i.e. copy, (1), kopia)")
    # duplicate_indicator = input()

    get_date(sourceFolder, destinationFolder)
