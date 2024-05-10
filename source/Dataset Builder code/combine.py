import json
import pandas as pd
jsonFilePath1 = r'/Users/ryan/Desktop/NLPFinalProject/Lexicon1 - w2w.json'
jsonFilePath2 = r'/Users/ryan/Desktop/NLPFinalProject/Lexicon2 - w2w.json'


with open(jsonFilePath1, 'r+') as f1:               # open the file
    data1 = json.load(f1)

with open(jsonFilePath2, 'r+') as f2:                # open the file       
    data2 = json.load(f2)
    
df1 = pd.DataFrame([data1])                      # Creating DataFrames
df2 = pd.DataFrame([data2])                      # Creating DataFrames

MergeJson = pd.concat([df1, df2], axis=1)         # Concat DataFrames

MergeJson.to_json("combinedLexicon.json")  


'''
def merge_JsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            result.extend(json.load(infile))

    with open('combinationLexicon.json', 'w') as output_file:
        json.dump(result, output_file)

merge_JsonFiles([jsonFilePath1, jsonFilePath2])
'''