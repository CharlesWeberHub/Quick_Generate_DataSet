import pandas as pd
import os
import copy
from datetime import datetime

monthly_data_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_monthly_csv/'
monthly_data_file_list = os.listdir(monthly_data_path)
monthly_data_file_list.sort()

genre_file_path = '/IV_append/extract_csv/genre_csv_output/'
genre_data_file_list = os.listdir(genre_file_path)
genre_data_file_list.sort()

games_features_path = '/Users/charles/PycharmProjects/Games_Research/add_ranking_company_age_colume/games-features(age_month6).csv'

genre_list = ['Action', 'Adventure', 'Early+Access', 'Ex+Early+Access', 'Free', 'Indie', 'Massively', 'RPG',
              'Simulation', 'Sports', 'Strategy']

age_list = ['Action', 'Adventure', 'Early+Access', 'Ex+Early+Access', 'Free', 'Indie', 'Massively', 'RPG',
            'Simulation', 'Sports', 'Strategy']

average_age_list = ['ave_age_Action', 'ave_age_Adventure', 'ave_age_Early+Access', 'ave_age_Ex+Early+Access',
                    'ave_age_Free', 'ave_age_Indie', 'ave_age_Massively', 'ave_age_RPG',
                    'ave_age_Simulation', 'ave_age_Sports', 'ave_age_Strategy']

games_features_df = pd.read_csv(games_features_path, index_col=0)

# 2018-05-01 to 2019-04-30
# print(monthly_file_list[28:40])

start_day = datetime(2018, 5, 1)
month_period = 30.41
monthly_data_file_list = monthly_data_file_list[28:40]

# store the whole genre data
genre_list_dic = {}

# the statistic of these months data
genre_statis_dic = {}

# the statistic of the age
age_statis_dic = {}

id_genre_statis_df = pd.DataFrame(columns=genre_list)
id_age_statis_df = pd.DataFrame(columns=age_list)
average_age_df = pd.DataFrame(columns=['hint'])

for i, _genre_file in enumerate(genre_data_file_list):
    genre_data_df = pd.read_csv(genre_file_path + _genre_file, index_col=0)
    genre_list_dic[genre_list[i]] = genre_data_df

for i, month_data in enumerate(monthly_data_file_list):

    age_add = i

    for i, _genre_tag in enumerate(genre_list):
        genre_statis_dic[genre_list[i]] = 0
        age_statis_dic[genre_list[i]] = 0

    month_data_df = pd.read_csv(monthly_data_path + month_data, index_col=0)[['ID', 'Game']]

    not_found_count = 0

    for index, row in month_data_df.iterrows():
        # find the ID whether exist in the data
        is_exist = False
        for key in genre_list_dic.keys():
            # df depends on key
            c_df = genre_list_dic[key]
            double_match = c_df.loc[c_df['ID'] == row['ID']]
            if double_match.shape[0] == 1:
                _date_ob = double_match['ReleaseDate'].iloc[0]
                # print(_date_ob)
                if _date_ob != '0000-00-00':
                    release_day = pd.to_datetime(_date_ob.strip())
                    _age = ((start_day - release_day) / month_period).days

                    c_count = genre_statis_dic[key]
                    c_count = c_count + 1
                    genre_statis_dic[key] = c_count

                    c_age = age_statis_dic[key]
                    c_age = c_age + _age + age_add
                    age_statis_dic[key] = c_age
                    is_exist = True

        if is_exist:
            continue

        not_found_count += 1

    print('not_found_count:' + str(not_found_count))

    id_genre_statis_df = id_genre_statis_df.append(
        [{'Action': genre_statis_dic['Action'], 'Adventure': genre_statis_dic['Adventure'],
          'Early+Access': genre_statis_dic['Early+Access'],
          'Ex+Early+Access': genre_statis_dic['Ex+Early+Access'],
          'Free': genre_statis_dic['Free'], 'Indie': genre_statis_dic['Indie'],
          'Massively': genre_statis_dic['Massively'], 'RPG': genre_statis_dic['RPG'],
          'Simulation': genre_statis_dic['Simulation'], 'Sports': genre_statis_dic['Sports'],
          'Strategy': genre_statis_dic['Strategy']}], ignore_index=True)

    id_age_statis_df = id_age_statis_df.append(
        [{'Action': age_statis_dic['Action'], 'Adventure': age_statis_dic['Adventure'],
          'Early+Access': age_statis_dic['Early+Access'], 'Ex+Early+Access': age_statis_dic['Ex+Early+Access'],
          'Free': age_statis_dic['Free'], 'Indie': age_statis_dic['Indie'],
          'Massively': age_statis_dic['Massively'], 'RPG': age_statis_dic['RPG'],
          'Simulation': age_statis_dic['Simulation'], 'Sports': age_statis_dic['Sports'],
          'Strategy': age_statis_dic['Strategy']}], ignore_index=True)
    # break
for i, _genre_tag in enumerate(genre_list):
    average_age_df[average_age_list[i]] = id_age_statis_df[_genre_tag].div(id_genre_statis_df[_genre_tag])

average_age_df = average_age_df.drop(["hint"], axis=1)

id_genre_statis_df.to_csv(
    '/Users/charles/PycharmProjects/Games_Research/IV_append/genre_mean_age_append_iv/' + 'genre_statis_mean_age(12 months).csv')
id_age_statis_df.to_csv(
    '/Users/charles/PycharmProjects/Games_Research/IV_append/genre_mean_age_append_iv/' + 'age_statis_mean_age(12 months).csv')
average_age_df.to_csv(
    '/Users/charles/PycharmProjects/Games_Research/IV_append/genre_mean_age_append_iv/' + 'average_age(12 months).csv')
