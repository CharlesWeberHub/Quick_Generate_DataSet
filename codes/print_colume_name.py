import pandas as pd
import xlsxwriter

xl = pd.ExcelFile('/Users/charles/PycharmProjects/Quick_Generate_DataSet/data/out_put_final/data_20200610.xlsx')
sheet_names=xl.sheet_names
print(xl.sheet_names)
s_0=xl.parse(sheet_names[0])
s_1=xl.parse(sheet_names[1])
s_2=xl.parse(sheet_names[2])
s_3=xl.parse(sheet_names[3])
s_4=xl.parse(sheet_names[4])

print(type(s_0))

s_0.to_csv('/Users/charles/PycharmProjects/Quick_Generate_DataSet/data/out_put_final/data_6_month_20170401-20170930.csv')

print(s_0.columns.values.tolist())