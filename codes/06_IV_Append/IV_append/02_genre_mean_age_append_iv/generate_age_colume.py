import pandas as pd
import os

genre_file_path = '/IV_append/extract_csv/genre_csv_output/'

genre_csv_list = os.listdir(genre_file_path)
genre_csv_list.sort()

print(genre_csv_list)

for i in range(0, len(genre_csv_list)):
    file_path=genre_file_path + genre_csv_list[i]
    print(file_path)
    genre_df=pd.read_csv(file_path, index_col=0)
    print(genre_df.info())