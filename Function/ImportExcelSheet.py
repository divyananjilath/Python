import xlrd
loc = ("path of file")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
for r in range(sheet.nrows):
	for c in range(sheet.ncols):
		print(sheet.cell_value(r,c))
