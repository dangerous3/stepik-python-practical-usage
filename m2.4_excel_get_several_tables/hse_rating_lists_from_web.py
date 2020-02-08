import xlrd
import xlwt
import urllib.request

results = {}
files = [
    ('1', 'https://www.hse.ru/data/2018/03/07/1165679773/%D0%A2%D0%B5%D0%BA%D1%83%D1%89%D0%B8%D0%B9%20%D1%80%D0%B5%D0%B9%D1%82%D0%B8%D0%BD%D0%B3%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D0%B4%D0%B0%D1%87%201%20%D0%BA%D1%83%D1%80%D1%81%201%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80%202017-2018.xlsx'),
    ('2', 'https://www.hse.ru/data/2018/03/07/1165680460/%D0%A2%D0%B5%D0%BA%D1%83%D1%89%D0%B8%D0%B9%20%D1%80%D0%B5%D0%B9%D1%82%D0%B8%D0%BD%D0%B3%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D0%B4%D0%B0%D1%87%202%20%D0%BA%D1%83%D1%80%D1%81%201%20%D1%81%D0%B5%D0%BC%D0%B5%D1%81%D1%82%D1%80%202017-2018%2007.03.2018.xlsx'),
    ('3', 'https://www.hse.ru/data/2018/03/07/1165666923/%D0%A2%D0%B5%D0%BA%D1%83%D1%89%D0%B8%D0%B9%20%D1%80%D0%B5%D0%B9%D1%82%D0%B8%D0%BD%D0%B3%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%B5%D1%80%D0%B5%D1%81%D0%B4%D0%B0%D1%87%203%20%D0%BA%D1%83%D1%80%D1%81%201%20%D1%81%D0%B5%D0%BC%202017-2018.xlsx')
]

allsubj = set()

for file in files:
    course, url = file
    urllib.request.urlretrieve(url, '../samples/testhse.xlsx')

    # Добавьте ваш путь к файлу
    rb = xlrd.open_workbook('/home/dangerous3/Загрузки/hse_4zhur.xlsx')

    # выбираем активный лист
    sheet = rb.sheet_by_index(0)

    # получаем значение первой ячейки A1
    val = sheet.row_values(0)[0]

    #print(val)

    #получаем список значений из всех записей
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    subjects = vals[9][17:-1]
    for subj in subjects:
        allsubj.add(subj + '-' + course)

    # выводим список предметов
    print(*subjects)

    for i in range(11, len(vals)):
        row = vals[i]
        name = row[2]
        grades = row[17:-1]
        if name not in results:
            results[name] = {}
        for j in range(len(subjects)):
            results[name][subjects[j] + '-' + course] = grades[j]
        # print(name, grades)
        # print(row)
    print(results)

allsubj = sorted(allsubj)

wrb = xlwt.Workbook()
wrs = wrb.add_sheet('Testsheet')

#в A1 записываем значение 'name'
wrs.write(0, 0, 'name')

for i in range(len(allsubj)):
    wrs.write(0, i + 1, allsubj[i])

rownum = 1

for name in results:
    wrs.write(rownum, 0, name)
    for subjnum in range(len(allsubj)):
        subj = allsubj[subjnum]
        if subj in results[name]:
            wrs.write(rownum, subjnum + 1, results[name][subj])
        else:
            wrs.write(rownum, subjnum + 1, '')
    rownum += 1

# сохраняем рабочую книгу
wrb.save('../samples/results.xlsx')

    # Выводим строки с информацией о первом студенте
    #print(*vals[11])