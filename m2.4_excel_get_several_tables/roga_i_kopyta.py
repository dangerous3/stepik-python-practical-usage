import xlrd
import zipfile
import os
import urllib.request
import collections

homepath = '/home/dangerous3/Загрузки'
zipdir = 'zipdir'
zipfile_url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
zipfile_name = 'rogaikopyta.zip'

os.chdir(homepath)
if os.path.exists(zipdir):
    pass
else:
    try:
        os.mkdir(zipdir)
    except OSError:
        print("Creation of the directory %s failed" % zipdir)
os.chdir(zipdir)

urllib.request.urlretrieve(zipfile_url, zipfile_name)

z = zipfile.ZipFile(zipfile_name)

z.extractall()

employee = {}

for i in range(1,1001):
    current_zip = str(i) + '.xlsx'
    wb = xlrd.open_workbook(current_zip, on_demand = True)
    sheet = wb.sheet_by_index(0)
    fio = sheet.cell_value(1,1)
    salary = int(sheet.cell_value(1,3))
    employee[fio] = salary
    wb.release_resources()
    del wb

ordered = collections.OrderedDict(sorted(employee.items()))

for name, wage in ordered.items():
    print(name, wage)






