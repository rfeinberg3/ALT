import csv
import json

# Decide the two file paths according to your 
# computer system
csvFilePath = r'/Users/ryan/Desktop/NLPFinalProject/Hittite Sheet - w2w.csv'
jsonFilePath = r'/Users/ryan/Desktop/NLPFinalProject/Hittite Sheet - w2w.json'
csvfile = open(csvFilePath, 'r')
jsonfile = open(jsonFilePath, 'w')

fieldnames = ("Hittite", "translation")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

'''
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = []
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            #=key = rows['No']
            #data[key] = rows
            data = rows
 
    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
# Driver Code
 

 
# Call the make_json function
make_json(csvFilePath, jsonFilePath)
'''