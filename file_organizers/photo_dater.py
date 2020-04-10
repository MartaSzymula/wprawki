"""This program changes .jpg and .nef files naming and moves them to directories named by dates when they were taken.
"""
import os
import shutil
import exifread
import argparse

def get_exif(folderName, filename):

    with open(f"{folderName}\\{filename}", 'rb') as image_file:
        tags = exifread.process_file(image_file)
    return tags


def get_date(date_tag):

    year = date_tag[0:4]
    month = date_tag[5:7]
    day = date_tag[8:10]
    date = f"{year}-{month}-{day}"
    return date


def get_file_name(number):

    if number <10:
        photo_num = "DSC_000" + str(number)

    elif number in range(9, 99):
        photo_num = "DSC_00" + str(number)

    elif number in range(100, 999):
        photo_num = "DSC_0" + str(number)

    else:
        photo_num = "DSC_" + str(number)

    return photo_num


def main(sourceFolder, destinationFolder):

    photo_list = []
    number = ""
    photo_count = {'jpg':0, 'nef':0}

    for folderName, subfolders, filenames in os.walk(sourceFolder):

        for filename in filenames:

            extension = filename.split('.')[-1].lower()

            if extension in ['jpg', 'nef']:

                tags = get_exif(folderName, filename)
                date_tag = str(tags['EXIF DateTimeOriginal'])
                date = get_date(date_tag)

                destination_path = f"{destinationFolder}/{extension}/{date}"

                photo_count[extension] += 1

                print(photo_count)

                new_photo_name = get_file_name(photo_count[extension])

                # Directory creation as suggested on: https://thispointer.com/how-to-create-a-directory-in-python/
                try:
                    if not os.path.isdir(f"{destinationFolder}/{extension}"):
                        os.mkdir(f"{destinationFolder}/{extension}")
                    os.mkdir(destination_path)
                    print("Directory " , destination_path ,  " created ")
                except FileExistsError:
                    print("Directory " , destination_path ,  " already exists")

                print(f"I\'m renaming file: {filename} to {new_photo_name}.{extension} and moving to folder {date}")

                shutil.move(f"{folderName}/{filename}", f"{destination_path}/{new_photo_name}.{extension}")


            else:
                print("Error processing file", filename)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='This program is for moving and renaming .jpg and .nef files.')

    parser.add_argument('--sourceFolder', type=str, default='C:/Users/Ja/Desktop/test-JP',
                        help='Path to folder with pictures.')
    parser.add_argument('--destinationFolder', type=str, default='C:/Users/Ja/Desktop/dest-JP',
                        help='Destination path for processed pictures')

    args = parser.parse_args()

    main(args.sourceFolder, args.destinationFolder)
