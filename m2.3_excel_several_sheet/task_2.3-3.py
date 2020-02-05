import xlrd

rb = xlrd.open_workbook('~/Загрузки/trekking2.xlsx')
sheet1 = rb.sheet_by_name('Справочник')
sheet2 = rb.sheet_by_name('Раскладка')

values1 = [sheet1.row_values(rownum) for rownum in range(sheet1.nrows)]
values2 = [sheet2.row_values(rownum) for rownum in range(sheet2.nrows)]
#print(values)

menu = {}
reference = {}

print(sheet2.nrows)

# Раскладка
for cols in range(1,sheet2.nrows):
    menu[sheet2.cell_value(cols,0)] = sheet2.cell_value(cols,1)
    print(sheet2.cell_value(cols,0), menu[sheet2.cell_value(cols,0)])
print(menu)

# Справочник
for cols in range(1,sheet1.nrows):
    reference[sheet1.cell_value(cols,0)] = sheet1.row_values(cols,1)


#print(reference)

calories = []
protein = []
fat = []
carbohydrates = []

for meal in menu.keys():
    #print(meal)
    calories.append(reference[meal][0])
    protein.append(reference[meal][1])
    fat.append(reference[meal][2])
    carbohydrates.append(reference[meal][3])
#print(calories, protein, fat, carbohydrates)



