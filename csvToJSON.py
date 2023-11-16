import csv
import json
import re

# Decide the two file paths according to your 
# computer system
csvFilePath = r'/Users/ryan/Desktop/NLPFinalProject/Hittite Sheet - w2w.csv'
jsonFilePath = r'/Users/ryan/Desktop/NLPFinalProject/Hittite Sheet - w2w.json'
csvfile = open(csvFilePath, 'r')
jsonfile = open(jsonFilePath, 'w')

fieldnames = ("Hittite", "Translation")
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    # use regex to scrub "Hittie" labeled data from csv
    pattern_hittite_text = r'\w+' 
    pattern_hittite = re.compile(pattern_hittite_text)
    hitRow = pattern_hittite.match(row["Hittite"]) # match only first word from "Hittite" labeled data

    pattern_translation_text = r'(\w+[;]?[^.]+)[.]{1}' 
    pattern_translation = re.compile(pattern_translation_text)
    translationRow = pattern_translation.match(row["Translation"]) # match definition up to first period. (; symbol shuld be included because it entails the same definition in a different light.)
    if hitRow != None:
        row["Hittite"] = hitRow.group(0)
    else:
        continue
    if translationRow != None:
        row["Translation"] = translationRow.group(0)
    else:
        continue
    json.dump(row, jsonfile)
    jsonfile.write('\n')
