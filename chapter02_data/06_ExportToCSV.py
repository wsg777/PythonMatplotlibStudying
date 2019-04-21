# 读json
import csv
import json

data = {}
filename = 'fileFor05.json'
with open(filename) as f:
    data = json.load(f)

# 写CSV方式1
filename2 = 'fileFor06.csv'
with open(filename2, 'w') as f:
    for key, value in data.items():
        line = key + ',' + value + '\n'
        f.write(line)

# 写CSV方式2
filename3 = 'fileFor06_2.csv'
csvFile = open(filename3, 'w', newline='')
try:
    writer = csv.writer(csvFile)
    for key, value in data.items():
        writer.writerow((key, value))
finally:
    csvFile.close()
