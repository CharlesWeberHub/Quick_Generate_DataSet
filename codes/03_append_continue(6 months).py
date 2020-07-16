import os
import pandas as pd

# to_csv时，设置index=False 或 index=True，index_label = 'id'
# read_csv时，设置index_col=0即可

remain_game_id_path = r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\out_put_remain_games\final(6).csv'
game_features_path = r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\sourse_game_features_dataset\games-features(age_month6).csv'

# 2019-06-01 to 2019-11-30
# print(monthly_file_list[41:47])

monthly_data_path = r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\source_calendar_data'
monthly_file_list = os.listdir(monthly_data_path)
monthly_file_list.sort()
monthly_file_list = monthly_file_list[41:47]
print(monthly_file_list)

remain_game_id_df = pd.read_csv(remain_game_id_path)
games_features_df = pd.read_csv(game_features_path)
remain_games_features_df = pd.DataFrame(columns=games_features_df.columns.values)
count = 0
for index, row in remain_game_id_df.iterrows():
    double_match = games_features_df.loc[games_features_df['QueryID'] == row['ID']]
    if double_match.shape[0] == 1:
        remain_games_features_df = remain_games_features_df.append(double_match)
        count += 1

remain_games_features_df.to_csv(r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\out_put_game_features\test.csv')

for i in range(len(monthly_file_list)):
    monthly_file_path = os.path.join(monthly_data_path, monthly_file_list[i])
    month_data_df = pd.read_csv(monthly_file_path)
    colume_name='Owner_change_from '+monthly_file_list[i][0:24]
    id_sales_df = pd.DataFrame(columns=[colume_name])
    remain_games_features_df[colume_name] = id_sales_df[colume_name]

    for index, row in remain_games_features_df.iterrows():
        id_match = month_data_df.loc[month_data_df['ID'] == row['QueryID']]
        current_index = remain_games_features_df[remain_games_features_df['QueryID'] == row['QueryID']].index[0]
        remain_games_features_df.loc[current_index, colume_name] = id_match['Sales'].iloc[0]

# # remain_games_features_df=remain_games_features_df.drop(['SupportURL'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['SupportEmail'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['AboutText'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['ShortDescrip'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['Background'],axis=1)
# # remain_games_features_df=remain_games_features_df.drop(['DetailedDescrip'],axis=1)
remain_games_features_df=remain_games_features_df.drop(['Unnamed: 0'],axis=1)
# remain_games_features_df=remain_games_features_df.drop(['Unnamed: 0.1'],axis=1)
# remain_games_features_df=remain_games_features_df.drop(['Unnamed: 0.1.1'],axis=1)
# remain_games_features_df=remain_games_features_df.drop(['Unnamed: 0.1.1.1'],axis=1)
# remain_games_features_df=remain_games_features_df.drop(['Unnamed: 0.1.1.1.1'],axis=1)
# remain_games_features_df=remain_games_features_df.reset_index()
# remain_games_features_df=remain_games_features_df.drop(['index'],axis=1)
print(remain_games_features_df.info())
remain_games_features_df.to_csv(r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\out_put_final\final(6_months).csv')
