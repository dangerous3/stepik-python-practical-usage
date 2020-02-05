import xlrd

rb = xlrd.open_workbook('~/Загрузки/trekking1.xlsx')
sheet = rb.sheet_by_name('Справочник')

values = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
#print(values)

meal = {}

#print(sheet.nrows)

for cols in range(1,sheet.nrows):
    meal[sheet.cell_value(cols,0)] = sheet.cell_value(cols,1)

list_meal = list(meal.items())
list_meal.sort(key=lambda i: (-i[1], i[0]))


for i in list_meal:
    print(i[0])


