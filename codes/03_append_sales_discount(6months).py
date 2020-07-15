import os
import pandas as pd
import np

# to_csv时，设置index=False 或 index=True，index_label = 'id'
# read_csv时，设置index_col=0即可

remain_game_id_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/final.csv'
games_features_path = '/Users/charles/PycharmProjects/Games_Research/add_ranking_company_age_colume/games-features(age_month6).csv'

# 2017-04-01 to 2017-09-30
# print(monthly_file_list[15:21])

monthly_file_path = '/Users/charles/PycharmProjects/Games_Research/Filter_Excel_From_HTML/OUTPUT_DATA/Calendar_monthly_csv/'
monthly_file_list = os.listdir(monthly_file_path)
monthly_file_list.sort()
monthly_file_list=monthly_file_list[15:21]
remain_game_id_df = pd.read_csv(remain_game_id_path,index_col=0)
games_features_df = pd.read_csv(games_features_path,index_col=0)

new_features=games_features_df.columns.values

new_features = np.append(new_features, np.array(['Max discount','Price','Sales']))

remain_games_features_df = pd.DataFrame(columns=new_features)
count = 0
for index, row in remain_game_id_df.iterrows():
    double_match = games_features_df.loc[games_features_df['QueryID'] == row['ID']]
    print(index)
    origin_age=double_match['age'].iloc[0]

    for i in range(len(monthly_file_list)):
        month_data_df = pd.read_csv(monthly_file_path + monthly_file_list[i],index_col=0)
        id_match = month_data_df.loc[month_data_df['ID'] == row['ID']]
        max_discount=id_match['Max discount'].iloc[0]
        sales=id_match['Sales'].iloc[0]
        price=id_match['Price'].iloc[0]
        c_age=origin_age+i
        # print(max_discount)
        # print(sales)
        # print(c_age)
        double_match['Max discount']=max_discount
        double_match['Price'] = price
        double_match['Sales']=sales
        double_match['age']=c_age

        #print(double_match)
        remain_games_features_df = remain_games_features_df.append(double_match,sort=False, ignore_index=True)


remain_games_features_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(6_months).csv')

