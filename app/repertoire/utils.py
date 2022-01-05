import os
import csv

from .models import File

path = "../../files"


def parse_directory(dir):
    dir_list = os.listdir(dir)

    return dir_list


def csv_to_dict(csvFilePath):
    dict_array = []

    # read csv file
    with open(csvFilePath, encoding="utf-8") as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            dict_array.append(row)

    return dict_array, len(dict_array)


def parse_file(path="files"):

    dir = parse_directory(path)
    files = []
    for filename in dir:
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath):
            file_dict, files_count = csv_to_dict(filepath)
            files.append(
                {"works": file_dict, "work_count": files_count, "filename": filename}
            )

    return files


def get_source(file: File):
    return file.filename.split(".")[0]
