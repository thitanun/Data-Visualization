from tabnanny import check
import pandas as pd
from datetime import *
from datetime import datetime

# from soupsieve import select
# file = 'Superstore.csv'
file = 'test20line.xls'
# read_file = pd.read_csv(file, encoding = 'windows-1254')
read_file = pd.read_excel(file,index_col=None)

file_head = list(read_file.head(0))
select_datename = ['Order Date']
list_headdate = [name_head for name_head in file_head if "DATE" in name_head.upper()] 

file_date = pd.DataFrame(read_file[select_datename])
file_date_all = pd.DataFrame(read_file[select_datename])

for i_date,k_date in enumerate(file_date.keys()):
    data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in file_date[k_date]]
    file_date[k_date] = data_date
    year_data = list(pd.DatetimeIndex(file_date[k_date]).year.drop_duplicates())
    year_data.sort()
    month_data = list(pd.DatetimeIndex(file_date[k_date]).month.drop_duplicates())
    month_data.sort()
    day_data = list(pd.DatetimeIndex(file_date[k_date]).day.drop_duplicates())
    day_data.sort()
print(year_data)
print(month_data)
print(day_data)

for i_date,k_date in enumerate(file_date_all.keys()):
    data_date = [datetime.strptime(date, "%d/%m/%Y").date() if type(date) == str else datetime.date(date)  for date in file_date_all[k_date]]
    file_date[k_date] = data_date
    year_data_all = list(pd.DatetimeIndex(file_date[k_date]).year)
    month_data = list(pd.DatetimeIndex(file_date[k_date]).month)
    month_data_all = list(pd.DatetimeIndex(file_date[k_date]).month)
    day_data_all = list(pd.DatetimeIndex(file_date[k_date]).day)

print(year_data_all)
print(month_data_all)
print(day_data_all)
    

# frame_new = {}
# for i,k in  enumerate(file_date.keys()):
#     check_month = [datetime.strftime(date, "%d/%m/%Y") for date in file_date[k] if date.month == 10 ]
#     frame_new[k] = check_month
# print(pd.DataFrame(frame_new))

        
        
    

    