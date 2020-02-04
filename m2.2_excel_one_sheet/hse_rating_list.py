import xlrd, xlwt

# Добавьте ваш путь к файлу
rb = xlrd.open_workbook('~/Загрузки/hse_4zhur.xlsx')

# выбираем активный лист
sheet = rb.sheet_by_index(0)

# получаем значение первой ячейки A1
val = sheet.row_values(0)[0]

print(val)

#получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

# выводим список предметов
print(*vals[9][13:])

# Выводим строки с информацией о первом студенте
print(*vals[11])