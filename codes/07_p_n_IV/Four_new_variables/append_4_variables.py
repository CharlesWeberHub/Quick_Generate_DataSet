import pandas as pd
import xlsxwriter

xl = pd.ExcelFile('/Users/charles/PycharmProjects/Scrap_Score/venv/output_file/data_20200424.xlsx')
sheet_names = xl.sheet_names
print(xl.sheet_names)
s_0 = xl.parse(sheet_names[0])
s_1 = xl.parse(sheet_names[1])
s_2 = xl.parse(sheet_names[2])
s_3 = xl.parse(sheet_names[3])
s_4 = xl.parse(sheet_names[4])

md_pub_df = pd.read_excel('/Users/charles/PycharmProjects/Scrap_Score/venv/Four_new_variables/mid_size_companies.xlsx')
major_company_df = pd.read_csv('/Users/charles/PycharmProjects/Scrap_Score/venv/Four_new_variables/MajorCompany.csv')

# print(md_pub_df.info())
# print(major_company_df.info())

mid_company_list_all = pd.concat(md_pub_df.iloc[:, i] for i in range(0, md_pub_df.shape[1]))
mid_company_list_all.index = pd.np.arange(len(mid_company_list_all))
mid_company_list_all = mid_company_list_all.dropna().unique().tolist()
mid_company_list_all = [item.lower() for item in mid_company_list_all]

major_company_list_all = pd.concat(major_company_df.iloc[:, i] for i in range(1, major_company_df.shape[1]))
major_company_list_all.index = pd.np.arange(len(major_company_list_all))
major_company_list_all = major_company_list_all.dropna().unique().tolist()
major_company_list_all = [item.lower() for item in major_company_list_all]

mid_company_list_2018 = md_pub_df['_2018'].dropna().tolist()
major_company_list_2018 = major_company_df['_2018'].dropna().tolist()

print(mid_company_list_2018)
print(major_company_list_2018)


def string_finder(columns, words):
    if any(word in field for field in columns for word in words):
        return 1
    return 0


# IsAAA is the same as your  IsMajorCompany. IsAAA =1 if major and 0 otherwise
# IsMidSize = 1 if mid-sized in any year, and 0 otherwise
# IsAAA_2018 is similar to  IsMajorCompany. IsAAA_2018 =1 if major in 2018 and 0 otherwise.
# IsMidSize_2018 =1 if mid-sized in 2018, and 0 otherwise.


s_0[['Publisher']] = s_0['Publisher'].str.lower()

major_company_list_all = [item.lower() for item in major_company_list_all]
mid_company_list_all = [item.lower() for item in mid_company_list_all]
major_company_list_2018 = [item.lower() for item in major_company_list_2018]
mid_company_list_2018 = [item.lower() for item in mid_company_list_2018]

s_0['IsAAA'] = s_0[['Publisher']].astype(str).apply(string_finder, words=major_company_list_all, axis=1)
s_0['IsMidSize'] = s_0[['Publisher']].astype(str).apply(string_finder, words=mid_company_list_all, axis=1)

s_0['IsAAA_2018'] = s_0[['Publisher']].astype(str).apply(string_finder, words=major_company_list_2018, axis=1)
s_0['IsMidSize_2018'] = s_0[['Publisher']].astype(str).apply(string_finder, words=mid_company_list_2018, axis=1)

# print(s_0.info())

s_0 = s_0.drop(['Unnamed: 0'], axis=1)

print(s_0[['IsAAA']].mean(axis=0))
print(s_0[['IsMidSize']].mean(axis=0))
print(s_0[['IsAAA_2018']].mean(axis=0))
print(s_0[['IsMidSize_2018']].mean(axis=0))

writer = pd.ExcelWriter('/Users/charles/PycharmProjects/Scrap_Score/venv/output_file/data_20200615.xlsx',engine='xlsxwriter')

s_0.to_excel(excel_writer=writer, sheet_name=sheet_names[0], encoding="utf-8", index=False)
s_1.to_excel(excel_writer=writer, sheet_name=sheet_names[1], encoding="utf-8", index=False)
s_2.to_excel(excel_writer=writer, sheet_name=sheet_names[2], encoding="utf-8", index=False)
s_3.to_excel(excel_writer=writer, sheet_name=sheet_names[3], encoding="utf-8", index=False)
s_4.to_excel(excel_writer=writer, sheet_name=sheet_names[4], encoding="utf-8", index=False)

writer.save()
writer.close()
