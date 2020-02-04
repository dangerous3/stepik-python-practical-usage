import xlrd
from statistics import mean, median

rb = xlrd.open_workbook('~/Загрузки/salaries.xlsx')
sheet = rb.sheet_by_index(0)

vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

max_median = 0
city_max_median = ''
max_mean = 0
profession_max_mean = ''

for rows in range(1,8):
    print(vals[rows][1:8])
    cur_median = median(vals[rows][1:7])
    #print("Населенный пункт: " + vals[rows][0] + "; Медиана: " + str(cur_median))
    if cur_median > max_median:
        max_median = cur_median
        city_max_median = vals[rows][0]

#for cols in range(1,7):
    #print(vals[cols][1:8])
    #cur_mean = mean(vals[1:8][cols])
    #print("Населенный пункт: " + vals[0][cols] + "; Среднее: " + str(cur_mean))
    #if cur_mean > max_mean:
        #max_mean = cur_mean
        #profession_max_mean = vals[0][cols]

print("Максимальная медиана равна: " + str(max_median) + ". Населенный пункт: " + city_max_median)
#print("Максимальное среднее равно: " + str(max_mean) + ". Профессия: " + city_max_mean)




