import pandas as pd
file_path='/Users/charles/PycharmProjects/Scrap_Score/venv/codes/file_for_conbine.csv'

file_df=pd.read_csv(file_path)

file_df.rename(columns={'meta_score':'new_meta_score','user_score':'new_user_score'},inplace=True)


file_df.to_csv('file_for_conbine(renamed).csv')