import pandas as pd

data_df=pd.read_csv('/Users/charles/PycharmProjects/Quick_Generate_DataSet/data/sourse_game_features_dataset/games-features(major_company).csv')

print(data_df[['isMajorCompany']][data_df[['isMajorCompany']]==True].info())