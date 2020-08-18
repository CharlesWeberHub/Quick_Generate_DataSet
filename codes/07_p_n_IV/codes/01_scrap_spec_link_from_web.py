import requests
from lxml import etree
import pandas as pd
import time

pre_url = "https://store.steampowered.com/app/"

_666_games_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/data/out_put_final/final_new_form(6_months_split_discount).xls'

_666_games_df = pd.read_excel(_666_games_path)
now_ID = 0
nnn = 0

id_url_df = pd.DataFrame(columns=['ID', 'URL'])

for index, row in _666_games_df[['QueryID']].iterrows():
    # print(row['QueryID'])
    if now_ID != row['QueryID']:
        now_ID = row['QueryID']
        url = pre_url + str(now_ID)
        meta_url = ''
        try:
            response = requests.get(url)
            html_str = response.text
            html = etree.HTML(html_str)
            for link in html.xpath('//a[contains(@href, "metacritic")]'):
                meta_url = link.attrib.get('href')
                print(now_ID)
                print(meta_url)

        except Exception as e:
            print(e)

        a_row = {"ID": now_ID, "URL": meta_url}
        id_url_df = id_url_df.append(a_row, ignore_index=True)

        nnn += 1
        if nnn >= 50:
            time.sleep(50)
            nnn = 0

id_url_df.to_excel('C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/id_meta_url(498_games).xls')

# x_path='/html/body/div[1]/div[7]/div[4]/div[1]/div[3]/div[5]/div[2]/div[9]/div/div[1]/div[3]/div[2]/a'
#
# meta_critic_url = html.xpath(x_path)
#
# print(meta_critic_url)
