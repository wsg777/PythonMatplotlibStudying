import xlrd

filename = 'ch02-xlsxdata.xlsx'
wb = xlrd.open_workbook(filename=filename)
ws = wb.sheet_by_name('Sheet1')
dataset = []
for r in range(ws.nrows):
    col = []
    for c in range(ws.ncols):
        col.append(ws.cell(r, c).value)
    dataset.append(col)

for line in dataset:
    print(line)

# from pprint import pprint
# pprint(dataset)
