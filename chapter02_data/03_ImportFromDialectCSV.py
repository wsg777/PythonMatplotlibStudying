# 存在问题！
import csv
filename = "ch02-data.tab"
data = []
try:
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            print(line.split('\t'))
        # reader = csv.reader(f, dialect=csv.excel_tab)
        # header = next(reader)
        # data = [row for row in reader]
        # print(header)
except csv.Error as e:
    # print("Error reading CSV file at line %s: %s" %(reader.line_num, e))
    exit(-1)

# if header:
#     print(header)
#     print("=================")
# for datarow in data:
#     print(datarow)


