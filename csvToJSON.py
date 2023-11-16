import csv
import json
import re

# Decide the two file paths according to your 
# computer system
csvFilePath = r'/Users/ryan/Desktop/NLPFinalProject/Hittite Sheet - w2w.csv'
jsonFilePath = r'/Users/ryan/Desktop/NLPFinalProject/Hittite Sheet - w2w.json'
csvfile = open(csvFilePath, 'r')
jsonfile = open(jsonFilePath, 'w')

reader = csv.DictReader( csvfile, fieldnames)
fieldnames = ("Hittite", "Translation")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    # use regex to scrub "Hittie" labeled data from csv
    pattern_text = r'\w+' 
    pattern = re.compile(pattern_text)
    hitScraped = pattern.match(row["Hittite"]) # match only first word from "Hittite" labeled data
    if hitScraped != None:
        row["Hittite"] = hitScraped.group(0)
    else:
        continue

    json.dump(row, jsonfile)
    jsonfile.write('\n')
