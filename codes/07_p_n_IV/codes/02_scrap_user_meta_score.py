import requests
from lxml import etree
import pandas as pd
import time

id_meta_url_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/id_meta_url(498_games).xls'
id_meta_url_df = pd.read_excel(id_meta_url_path)

id_results = pd.DataFrame(
    columns=['ID', 'meta_score', 'num_critic_reviews', 'user_score', 'num_ratings', 'critic_positive', 'critic_mixed',
             'critic_negative', 'user_positive', 'user_mixed', 'user_negative'])

nnn = 0
file_count = 3

for index, row in id_meta_url_df.iterrows():
    print(index)
    _id = row['ID']
    print('ID:  ' + str(_id))
    test_url = row['URL']
    html_str = ''
    try:
        print(test_url)
        response = requests.get(test_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
        html_str = response.text
    except Exception as e:
        continue

    html = etree.HTML(html_str)
    meta_score = html.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/a/div/span')
    meta_score_str = '0'
    try:
        meta_score_str = meta_score[0].text.strip()
    except Exception as e:
        print(e)
        # meta_score = html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[1]/div/div/a/div/span')
        meta_score = html.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[1]/div/div/a/div/span')
        print(meta_score)
        try:
            meta_score_str = meta_score[0].text.strip()
        except Exception as e:
            continue

    print(meta_score_str)

    num_critic_reviews = html.xpath(
        '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/p/span[2]/a/span')
    num_critic_reviews_str = '0'
    try:
        num_critic_reviews_str = num_critic_reviews[0].text.strip()
    except Exception as e:
        print(e)
        num_critic_reviews = html.xpath(
            '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[1]/div/div/div[2]/p/span[2]/a/span')
        num_critic_reviews_str = num_critic_reviews[0].text.strip()

    print(num_critic_reviews_str)

    user_score = html.xpath('//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/a/div')
    user_score_str = '0'
    try:
        user_score_str = user_score[0].text.strip()
    except Exception as e:
        print(e)
        user_score = html.xpath(
            '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/a/div')
        try:
            user_score_str = user_score[0].text.strip()
        except Exception as e:
            continue
    print(user_score_str)

    num_ratings = html.xpath(
        '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/p/span[2]/a')
    num_ratings_str = '0'
    try:
        num_ratings_str = num_ratings[0].text.strip()
    except Exception as e:
        print(e)
        num_ratings = html.xpath(
            '//*[@id="main"]/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/p/span[2]/a')
        try:
            num_ratings_str = num_ratings[0].text.strip()
        except Exception as e:
            continue
    print(num_ratings_str)

    critic_positive = html.xpath(
        '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/div[2]/div/div/ol/li[1]/div/span[2]/a/span/span[1]')
    critic_positive_str = '0'
    try:
        critic_positive_str = critic_positive[0].text.strip()
    except Exception as e:
        print(e)
    print(critic_positive_str)

    critic_mixed = html.xpath(
        '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/div[2]/div/div/ol/li[2]/div/span[2]/a/span/span[1]')
    critic_mixed_str = '0'
    try:
        critic_mixed_str = critic_mixed[0].text.strip()
    except Exception as e:
        print(e)
    print(critic_mixed_str)

    critic_negative = html.xpath(
        '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[1]/div[2]/div/div/ol/li[3]/div/span[2]/a/span/span[1]')
    critic_negative_str = '0'
    try:
        critic_negative_str = critic_negative[0].text.strip()
    except Exception as e:
        print(e)
    print(critic_negative_str)

    user_positive = html.xpath(
        '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/div/div/ol/li[1]/div/span[2]/a/span/span[1]')
    user_positive_str = '0'
    try:
        user_positive_str = user_positive[0].text.strip()
    except Exception as e:
        print(e)
    print(user_positive_str)

    user_mixed = html.xpath(
        '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/div/div/ol/li[2]/div/span[2]/a/span/span[1]')
    user_mixed_str = '0'
    try:
        user_mixed_str = user_mixed[0].text.strip()
    except Exception as e:
        print(e)
    print(user_mixed_str)

    user_negative = html.xpath(
        '//*[@id="main"]/div/div[3]/div[1]/div[1]/div/div[2]/div[3]/div/div/ol/li[3]/div/span[2]/a/span/span[1]')
    user_negative_str = '0'
    try:
        user_negative_str = user_negative[0].text.strip()
    except Exception as e:
        print(e)
    print(user_negative_str)

    a_row = {'ID': _id, 'meta_score': meta_score_str, 'num_critic_reviews': num_critic_reviews_str,
             'user_score': user_score_str, 'num_ratings': num_ratings_str, 'critic_positive': critic_positive_str,
             'critic_mixed': critic_mixed_str, 'critic_negative': critic_negative_str,
             'user_positive': user_positive_str, 'user_mixed': user_mixed_str, 'user_negative': user_negative_str}
    id_results = id_results.append(a_row, ignore_index=True)

    nnn += 1
    if nnn >= 40:
        file_count += 1
        out_put_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/temp/scores(498_games)_' + str(
            file_count) + '.xls'
        id_results.to_excel(out_put_path)
        id_results = pd.DataFrame(
            columns=['ID', 'meta_score', 'num_critic_reviews', 'user_score', 'num_ratings', 'critic_positive',
                     'critic_mixed', 'critic_negative', 'user_positive', 'user_mixed', 'user_negative'])
        time.sleep(50)
        nnn = 0

out_put_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/scores(498_games)_' + 'final' + '.xls'
id_results.to_excel(out_put_path)
