import xlrd, xlwt

results = {}

# Добавьте ваш путь к файлу
rb = xlrd.open_workbook('~/Загрузки/hse_4zhur.xlsx')

# выбираем активный лист
sheet = rb.sheet_by_index(0)

# получаем значение первой ячейки A1
val = sheet.row_values(0)[0]

#print(val)

#получаем список значений из всех записей
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
subjects = vals[9][17:-1]

# выводим список предметов
print(*subjects)

for i in range(11, len(vals)):
    row = vals[i]
    name = row[2]
    grades = row[17:-1]
    if name not in results:
        results[name] = {}
    for j in range(len(subjects)):
        results[name][subjects[j] + '-4'] = grades[j]
    # print(name, grades)
    # print(row)
print(results)

# Выводим строки с информацией о первом студенте
#print(*vals[11])