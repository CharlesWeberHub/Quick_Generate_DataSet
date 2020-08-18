import pandas as pd
import xlsxwriter

xl = pd.ExcelFile('/Users/charles/PycharmProjects/Scrap_Score/venv/output_file/data_20200424.xlsx')
sheet_names=xl.sheet_names
print(xl.sheet_names)
s_0=xl.parse(sheet_names[0])
s_1=xl.parse(sheet_names[1])
s_2=xl.parse(sheet_names[2])
s_3=xl.parse(sheet_names[3])
s_4=xl.parse(sheet_names[4])

pre_to_be_combine_df=pd.read_csv('/Users/charles/PycharmProjects/Scrap_Score/venv/codes/file_for_conbine(renamed).csv')

s_0['positive_count']=pre_to_be_combine_df[['positive_count']]
s_0['negative_count']=pre_to_be_combine_df[['negative_count']]
s_0['new_meta_score']=pre_to_be_combine_df[['new_meta_score']]
s_0['num_critic_reviews']=pre_to_be_combine_df[['num_critic_reviews']]
s_0['new_user_score']=pre_to_be_combine_df[['new_user_score']]
s_0['num_ratings']=pre_to_be_combine_df[['num_ratings']]
s_0['critic_positive']=pre_to_be_combine_df[['critic_positive']]
s_0['critic_mixed']=pre_to_be_combine_df[['critic_mixed']]
s_0['critic_negative']=pre_to_be_combine_df[['critic_negative']]
s_0['user_positive']=pre_to_be_combine_df[['user_positive']]
s_0['user_mixed']=pre_to_be_combine_df[['user_mixed']]
s_0['user_negative']=pre_to_be_combine_df[['user_negative']]

s_0=s_0.drop(['Unnamed: 0'],axis=1)
s_1=s_1.drop(['Unnamed: 0'],axis=1)
s_2=s_2.drop(['Unnamed: 0'],axis=1)
#s_3=s_3.drop(['Unnamed: 0'],axis=1)
#s_4=s_4.drop(['Unnamed: 0'],axis=1)

# print(s_0)
# print(s_1)
# print(s_2)

# s_0['positive_count', 'negative_count', 'new_meta_score', 'num_critic_reviews', 'new_user_score', 'num_ratings', 'critic_positive', 'critic_mixed',
#              'critic_negative', 'user_positive', 'user_mixed', 'user_negative']=pre_to_be_combine_df[['positive_count', 'negative_count', 'new_meta_score', 'num_critic_reviews', 'new_user_score', 'num_ratings', 'critic_positive', 'critic_mixed',
#              'critic_negative', 'user_positive', 'user_mixed', 'user_negative']]

writer = pd.ExcelWriter('/Users/charles/PycharmProjects/Scrap_Score/venv/output_file/data_20200610.xlsx',engine='xlsxwriter')

s_0.to_excel(excel_writer=writer, sheet_name=sheet_names[0], encoding="utf-8", index=False)
s_1.to_excel(excel_writer=writer, sheet_name=sheet_names[1], encoding="utf-8", index=False)
s_2.to_excel(excel_writer=writer, sheet_name=sheet_names[2], encoding="utf-8", index=False)
s_3.to_excel(excel_writer=writer, sheet_name=sheet_names[3], encoding="utf-8", index=False)
s_4.to_excel(excel_writer=writer, sheet_name=sheet_names[4], encoding="utf-8", index=False)

writer.save()
writer.close()

# print(s_0.info())
# print(s_1.info())
# print(s_2.info())
# print(s_3.info())
# print(s_4.info())

