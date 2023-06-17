#!/usr/bin/env python

# Gets sitemap created at task_2 and convert csv file to json

import csv
import json

def readCsvFile(filePath):
    with open(filePath, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    return data

def writeJsonFile(data, filePath):
    with open(filePath, 'w') as json_file:
        json.dump(data, json_file)

def convertCSVtoJsonFile(csvFilePath, jsonFilePath):
    csvData = readCsvFile(csvFilePath)
    writeJsonFile(csvData, jsonFilePath)

convertCSVtoJsonFile("./sitemap.csv", "./sitemap.json")