import pandas as pd
import os

six_months_file_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/data/out_put_final/final_new_form(6_months_split_discount).xls'
six_months_static_file_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/06_IV_Append/IV_append/02_genre_mean_age_append_iv/average_age(6 months 201906-201911).csv'
genre_file_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/06_IV_Append/IV_append/01_a_extract_csv/genre_csv_output/'

genre_data_file_list = os.listdir(genre_file_path)
genre_data_file_list.sort()

genre_list = ['ave_age_Action', 'ave_age_Adventure', 'ave_age_Early+Access', 'ave_age_Ex+Early+Access', 'ave_age_Free',
              'ave_age_Indie', 'ave_age_Massively', 'ave_age_RPG',
              'ave_age_Simulation', 'ave_age_Sports', 'ave_age_Strategy']

# store the whole genre data
genre_list_dic = {}

# give value to genre_list_dic
for i, _genre_file in enumerate(genre_data_file_list):
    genre_data_df = pd.read_csv(genre_file_path + _genre_file, index_col=0)['ID']
    id_list = genre_data_df.tolist()
    id_set = set(id_list)
    genre_list_dic[genre_list[i]] = id_set

# read the id we need to matched with genre
six_months_game_df = pd.read_excel(six_months_file_path, index_col=0)

# read the statistic data we need to matched with genre
six_months_static_df = pd.read_csv(six_months_static_file_path, index_col=0)

# the dataframe is to store the IVS
genre_IV_df = pd.DataFrame(columns=genre_list)

# pop id one by one
for index, row in six_months_game_df.iterrows():
    if (index + 1) % 6 != 1:
        continue

    six_months_static_copy_df = six_months_static_df.copy()
    # the list is used to match the statistic file
    genre_set_0_list = genre_list.copy()
    now_id = row['QueryID']
    # get the whole genres
    for key in genre_list_dic.keys():
        # judge which genre the id should be
        if now_id in genre_list_dic[key]:
            # remove the genre that has the data
            genre_set_0_list.remove(key)
    six_months_static_copy_df[genre_set_0_list] = 0
    print(six_months_static_copy_df)
    genre_IV_df = genre_IV_df.append(six_months_static_copy_df)

genre_IV_df = genre_IV_df.reset_index()
genre_IV_df = genre_IV_df.drop(['index'], axis=1)
# genre_IV_df.rename(columns={'Action':'IV_count_Action','Adventure':'IV_count_Adventure','Early+Access':'IV_count_Early+Access','Ex+Early+Access':'IV_count_Ex+Early+Access','Free':'IV_count_Free','Indie':'IV_count_Indie','Massively':'IV_count_Massively','RPG':'IV_count_RPG','Simulation':'IV_count_Simulation','Sports':'IV_count_Sports','Strategy':'IV_count_Strategy'},inplace=True)
# print(genre_IV_df.info())

genre_IV_df.to_csv(
    'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/06_IV_Append/IV_append/03_genre_append_ave_age_iv/IV_ave_age_6_months(201906-201911).csv')