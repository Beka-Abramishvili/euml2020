# -*- coding: utf-8 -*-

"""
import pandas as pd
excel_file = 'movies.xls'
#movies = pd.read_excel(excel_file)

#print(movies[:20].head(50))
movies_sheet1 = pd.read_excel(excel_file, sheet_name=1)
print(movies_sheet1.head(7))
print(movies_sheet1.shape)

xlsx = pd.ExcelFile(excel_file)
movies_sheets = []
for sheet in xlsx.sheet_names:
   movies_sheets.append(xlsx.parse(sheet))
movies = pd.concat(movies_sheets)

print(movies.head())
print(movies.shape)
"""


import pandas as pd
import matplotlib.pyplot as plt
excel_file = 'persons.xlsx'
persons = pd.read_excel(excel_file)
#print(persons.shape)
#persons.columns = ["Name", "Id"];   
#print(persons.head(persons.shape[0]))
sorted_by_sallary = persons.sort_values(['Sallary'], ascending=True)
sallary = sorted_by_sallary["Sallary"].head(10)
#print(sallary)
#sallary.plot(kind="hist")
#plt.show()
#print(persons.describe())


import numpy

ages = [70,76,80,85,85,85,95,96,100,108]

x = numpy.percentile(ages, 10)

print(x)  






















