import requests
import json
from contextlib import closing
import pandas as pd
import os
import copy
import types
from urllib.request import urlopen
import time
import random

# url = 'https://store.steampowered.com/appreviewhistogram/730?l=english&review_score_preference=0'

pre_url = 'https://store.steampowered.com/appreviewhistogram/'
lat_url = '?l=english&review_score_preference=0'

_666_games_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/data/out_put_final/final_new_form(6_months_split_discount).xls'

_666_games_df = pd.read_excel(_666_games_path)

now_ID = 0
nnn = 0

for index, row in _666_games_df[['QueryID']].iterrows():
    # print(row['QueryID'])
    if now_ID != row['QueryID']:
        now_ID = row['QueryID']
        url = pre_url + str(now_ID) + lat_url
        print(url)
        try:
            data = urlopen(url).read()
            bs = str(data, encoding="utf8")
            output_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/time_p_n_json/' + str(now_ID) + '.json'
            file = open(output_path, "w")
            file.write(bs)
            file.close()

        except Exception as e:
            print(e)
        nnn += 1
        if nnn >= 50:
            time.sleep(50)
            nnn = 0

# try:
#     data = urlopen(url).read()
#     print(data)
#     bs = str(data, encoding="utf8")
#     print(bs)
#     file = open("test.json", "w")
#     file.write(bs)
#     file.close()
#
# except Exception as e:
#     print(e)
