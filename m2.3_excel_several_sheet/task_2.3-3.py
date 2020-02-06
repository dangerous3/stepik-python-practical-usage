import xlrd
from collections import defaultdict
import math

rb = xlrd.open_workbook('~/Загрузки/trekking2.xlsx')
sheet1 = rb.sheet_by_name('Справочник')
sheet2 = rb.sheet_by_name('Раскладка')

values1 = [sheet1.row_values(rownum) for rownum in range(sheet1.nrows)]
values2 = [sheet2.row_values(rownum) for rownum in range(sheet2.nrows)]
#print(values)

menu = defaultdict(list)
reference = {}
menu_item = []


# Раскладка
for cols in range(1,sheet2.nrows):
    menu[sheet2.cell_value(cols,0)].append(sheet2.cell_value(cols,1))
print('Раскладка по меню на сегодня: {}'.format(menu))


# Справочник
for cols in range(1,sheet1.nrows):
    reference[sheet1.cell_value(cols,0)] = sheet1.row_values(cols,1)
    # Меняем пустые строки на 0
    for i, sublist in enumerate(reference[sheet1.cell_value(cols,0)]):
        if sublist == '':
            reference[sheet1.cell_value(cols, 0)][i] = 0
print('Справочник продуктов: {}'.format(reference))



def sum_of_nutrients(nutrient):
    #component_num_column: 0 - calories, 1 - protein, 2 - fat, 3 - carbohydrate
    result_list = []
    for key, value in menu.items():
        result_list.append(list(map(lambda x: x / 100 * reference[key][nutrient], value)))
    return [float(sum(j)) for j in zip(*result_list)]

for i in range(4):
    print(math.floor(*sum_of_nutrients(i)), end=" ")



