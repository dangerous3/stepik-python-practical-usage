import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import xlrd


wb = xlrd.open_workbook('../samples/results.xlsx')
sheet = wb.sheet_by_index(0)
subjs = sheet.row_values(0)
grades = {}
for subj in subjs[1:]:
    grades[subj] = [0, 0]
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    for i in range(1, len(subjs)):
        if isinstance(row[i], float):
            grades[subjs[i]][0] += row[i]
            grades[subjs[i]][1] += 1

mvals = []
for subj in subjs[1:]:
    if grades[subj][1] != 0:
        mvals.append(grades[subj][0] / grades[subj][1])

plt.plot(mvals)
x = list(range(len(subjs) - 1))
plt.xticks(x, subjs[1:], rotation='vertical')
plt.ylabel('some numbers')

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 15.5)

fig.autofmt_xdate(rotation = 25)

plt.savefig('../samples/foo.png', dpi=100)