import os

import csv
import json
path = "../../files"


def parse_directory(dir):
    dir_list = os.listdir(dir)

    return dir_list


def csv_to_dict(csvFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
    
    return jsonArray


def parse_file(path="../../files"):
    dir = parse_directory(path)
    files = []
    for file in dir:
        filename = os.path.join(path, file)
        if os.path.isfile(filename):
            file_dict = csv_to_dict(filename)
            files.append(file_dict)

    return files

print(parse_file())