"""This program takes
"""
import os
from PIL.ExifTags import TAGS
from PIL import Image
import shutil
import exif
import exifread

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
                    # year = '1970'
                    # month = '01'
                    # day = '01'

                # Directory creation as suggested on: https://thispointer.com/how-to-create-a-directory-in-python/

                date = f"{year}-{month}-{day}"

                try:
                    os.mkdir(f"{destinationFolder}/{date}")
                    print("Directory " , f"{destinationFolder}/{date}" ,  " created ")
                except FileExistsError:
                    print("Directory " , f"{destinationFolder}/{date}" ,  " already exists")

                photo_list.append(filename)

                number = len(photo_list)
                new_photo_name = enumeration(number)
                print(f"I\'m renaming file: {filename} to {new_photo_name}.jpg and moving to foler {date}")

                # shutil.move(f"{folderName}/{filename}", f"{destinationFolder}/{date}/{new_photo_name}.jpg")

            elif filename.split('.')[-1].lower() == 'nef':

                with open(f"{folderName}\\{filename}", 'rb') as image_file:

                    tags = exifread.process_file(image_file)

                    exif = str(tags['EXIF DateTimeOriginal'])

                    year = exif[0:4]
                    month = exif[5:7]
                    day = exif[8:10]

                    date = f"{year}-{month}-{day}"
                    # print(date)

                photo_list.append(filename)

                number = len(photo_list)
                new_photo_name = enumeration(number)
                print(f"I\'m renaming file: {filename} to {new_photo_name}.nef and moving to foler {date}")

                # shutil.move(f"{folderName}/{filename}", f"{destinationFolder}/{date}/{new_photo_name}.nef")


if __name__ == '__main__':

    sourceFolder = 'C:/Users/Ja/Desktop/test-JP'
    destinationFolder = 'C:/Users/Ja/Desktop/dest-JP'
    # print("Please input duplicate indicator (i.e. copy, (1), kopia)")
    # duplicate_indicator = input()

    get_date(sourceFolder, destinationFolder)
