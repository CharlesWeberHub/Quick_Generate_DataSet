import os
import pandas as pd
import xlsxwriter


total_data_file_path = '/Users/charles/PycharmProjects/Games_Research/IV_append/data_20200408.xlsx'

ave_age_6_months='/Users/charles/PycharmProjects/Games_Research/IV_append/genre_append_ave_age_iv/IV_ave_age_6_months.csv'
ave_age_12_months='/Users/charles/PycharmProjects/Games_Research/IV_append/genre_append_ave_age_iv/IV_ave_age_12_months.csv'
ave_age_6_quarters='/Users/charles/PycharmProjects/Games_Research/IV_append/genre_append_ave_age_iv/IV_ave_age_6_quarters.csv'

count_6_months='/Users/charles/PycharmProjects/Games_Research/IV_append/genre_append_iv/IV_count_6_months.csv'
count_12_months='/Users/charles/PycharmProjects/Games_Research/IV_append/genre_append_iv/IV_count_12_months.csv'
count_6_quarters='/Users/charles/PycharmProjects/Games_Research/IV_append/genre_append_iv/IV_count_6_quarters.csv'



sheet_list = ['6_months', '12_months', '6_quarters', 'Periods', 'Statista']

count_genre_list=['IV_count_Action','IV_count_Adventure','IV_count_Early+Access','IV_count_Ex+Early+Access','IV_count_Free','IV_count_Indie','IV_count_Massively','IV_count_RPG','IV_count_Simulation','IV_count_Sports','IV_count_Strategy']
age_genre_list = ['ave_age_Action', 'ave_age_Adventure', 'ave_age_Early+Access', 'ave_age_Ex+Early+Access', 'ave_age_Free', 'ave_age_Indie', 'ave_age_Massively', 'ave_age_RPG',
            'ave_age_Simulation', 'ave_age_Sports', 'ave_age_Strategy']
_6_months_df = pd.read_excel(total_data_file_path, sheet_name=sheet_list[0])
_12_months_df = pd.read_excel(total_data_file_path, sheet_name=sheet_list[1])
_6_quarters_df = pd.read_excel(total_data_file_path, sheet_name=sheet_list[2])
_periods_df = pd.read_excel(total_data_file_path, sheet_name=sheet_list[3])
_statista_df = pd.read_excel(total_data_file_path, sheet_name=sheet_list[4])

count_6_months_df=pd.read_csv(count_6_months, index_col=0)
count_12_months_df=pd.read_csv(count_12_months, index_col=0)
count_6_quarters_df=pd.read_csv(count_6_quarters, index_col=0)

ave_age_6_months_df=pd.read_csv(ave_age_6_months, index_col=0)
ave_age_12_months_df=pd.read_csv(ave_age_12_months, index_col=0)
ave_age_6_quarters_df=pd.read_csv(ave_age_6_quarters, index_col=0)

_6_months_df[count_genre_list]=count_6_months_df[count_genre_list]
_6_months_df[age_genre_list]=ave_age_6_months_df[age_genre_list]

_12_months_df[count_genre_list]=count_12_months_df[count_genre_list]
_12_months_df[age_genre_list]=ave_age_12_months_df[age_genre_list]

_6_quarters_df[count_genre_list]=count_6_quarters_df[count_genre_list]
_6_quarters_df[age_genre_list]=ave_age_6_quarters_df[age_genre_list]

_6_months_df.to_csv('1.csv', index=False)
_12_months_df.to_csv('2.csv', index=False)
_6_quarters_df.to_csv('3.csv', index=False)

print(_6_months_df.info())
print(_12_months_df.info())
print(_6_quarters_df.info())

writer = pd.ExcelWriter('data_20200424.xlsx',engine='xlsxwriter')

_6_months_df.to_excel(excel_writer=writer, sheet_name=sheet_list[0], encoding="utf-8", index=False)
_12_months_df.to_excel(excel_writer=writer, sheet_name=sheet_list[1], encoding="utf-8", index=False)
_6_quarters_df.to_excel(excel_writer=writer, sheet_name=sheet_list[2], encoding="utf-8", index=False)
_periods_df.to_excel(excel_writer=writer, sheet_name=sheet_list[3], encoding="utf-8", index=False)
_statista_df.to_excel(excel_writer=writer, sheet_name=sheet_list[4], encoding="utf-8", index=False)

writer.save()
writer.close()
