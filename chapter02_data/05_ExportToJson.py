# 读csv
import csv
import json

data = {}
filename = 'ch02-data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        data[row[0]] = row[1]

# 写json
filename2 = 'fileFor05.json'
with open(filename2, 'w') as f_obj:
    json.dump(data, f_obj)

