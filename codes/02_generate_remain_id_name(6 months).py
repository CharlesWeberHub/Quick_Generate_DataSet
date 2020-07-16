import pandas as pd
import os
import copy

monthly_data_path = r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\source_calendar_data'
game_features_path = r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\sourse_game_features_dataset\games-features(age_month6).csv'

monthly_data_file_list = os.listdir(monthly_data_path)
monthly_data_file_list.sort()

use_period = ''
use_count = 0
game_id_list_max = list()

game_features_df = pd.read_csv(game_features_path)

for i in range(len(monthly_data_file_list)):

    game_id_set = set()

    if 6 + i > len(monthly_data_file_list):
        break

    period = monthly_data_file_list[0 + i][0:13] + monthly_data_file_list[5 + i][13:24]

    game_id_list = {}
    for i, file in enumerate(monthly_data_file_list[0 + i:6 + i]):
        monthly_file_path = os.path.join(monthly_data_path, file)
        if i == 0:
            game_id_list = pd.read_csv(monthly_file_path)['ID'].tolist()
            game_id_set = set(game_id_list)
        else:
            game_id_list = pd.read_csv(monthly_file_path)['ID'].tolist()
            current_game_set = set(game_id_list)
            game_id_set = game_id_set&current_game_set

    game_id_set_copy = copy.copy(game_id_set)

    for index, value in enumerate(game_id_set_copy):
        id_match = game_features_df.loc[game_features_df['QueryID'] == value]
        if id_match.shape[0] != 1:
            game_id_set.remove(value)

    set_len = len(game_id_set)

    if period == '2019-06-01 to 2019-11-30':
        use_period = period
        use_count = set_len
        game_id_list_max = list(game_id_set)

    print(period + '  -------  remain_games:' + str(set_len))

print('use_period: ' + str(use_period))
print('use_count: ' + str(use_count))

name = ['ID']
game_id_list_max_df = pd.DataFrame(columns=name, data=game_id_list_max)
game_id_list_max_df.to_csv(r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\out_put_remain_games\final('
                           r'6).csv')
