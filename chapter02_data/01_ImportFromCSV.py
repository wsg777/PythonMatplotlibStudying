import csv
filename = "ch02-data.csv"
data = []
try:
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        data = [row for row in reader]
        print(data)
except csv.Error as e:
    print("Error reading CSV file at line %s: %s" %(reader.line_num, e))
    exit(-1)

if header:
    print(header)
    print("=================")
for datarow in data:
    print(datarow)

