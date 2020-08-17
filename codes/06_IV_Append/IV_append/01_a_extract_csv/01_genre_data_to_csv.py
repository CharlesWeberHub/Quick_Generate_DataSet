import os
import pandas as pd
from bs4 import BeautifulSoup

genre_file_path = '/Users/charles/PycharmProjects/Games_Research/IV_append/data_sourse/'
genre_excel_output_path = '/IV_append/01_extract_csv/genre_excel/'
output_path = '/IV_append/extract_csv/genre_csv_output/'

genre_file_list = os.listdir(genre_file_path)
genre_file_list.sort()

genre_csv_list = os.listdir(genre_excel_output_path)
genre_csv_list.sort()

print(genre_csv_list)

for i in range(0, len(genre_file_list)):
    output_file = output_path + genre_csv_list[i]

    print(output_file)
    c_genre_csv_df = pd.read_csv(genre_excel_output_path + genre_csv_list[i])
    genre_config_df = pd.DataFrame(columns=['ID', 'Game', 'ReleaseDate', 'Developer', 'Publisher'])

    html_file = open(genre_file_path + genre_file_list[i], 'r', encoding='utf-8')
    html_handle = html_file.read()
    soup = BeautifulSoup(html_handle, 'lxml')
    all_tr = soup.find_all('tr')

    is_to_scripe = False
    current_index = -1

    # to get the start index
    for tr_item in all_tr:
        if is_to_scripe:
            break
        current_index += 1
        try:
            tr_item.find('a')['href'].strip()
        except:
            continue
        href = tr_item.find('a')['href'].strip()
        if len(href) <= 25:
            continue
        if href[21:24] != 'app':
            continue
        is_to_scripe = True
        break
    # how many items we have
    _count = 0
    # the count we need to have
    # print()

    while _count < c_genre_csv_df.shape[0]:
        td_all_0 = all_tr[current_index].find_all('td')

        # IV we need to scripe
        _id = ''
        _game = ''
        _treleasedate = ''
        _developers = ''
        _publishers = ''

        for i, child in enumerate(td_all_0):
            # print(i, 'tt--', child)
            is_stop_first=False
            if i == 1:
                try:
                    _hf = child.find('a')['href'].strip()
                except:
                    print('except')
                    current_index += 1
                    is_stop_first=True
                    continue

                if len(_hf) <= 25:
                    continue
                if _hf[21:24] != 'app':
                    continue

                _id = _hf[25:]
                all_in_span = child.find_all('span', class_='html-attribute-value')
                _game = all_in_span[0].get_text()

        if is_stop_first:
            continue

        current_index += 1

        td_all_1 = all_tr[current_index].find_all('td')
        for i, child in enumerate(td_all_1):
            if i == 1:
                all_in_span = child.find_all('span', class_='html-attribute-value')
                _treleasedate = all_in_span[1].get_text()

        current_index += 1

        td_all_2 = all_tr[current_index].find_all('td')
        for i, child in enumerate(td_all_2):
            if i == 1:
                all_in_span = child.find_all('span', class_='html-attribute-value')
                try:
                    _developers = all_in_span[7].get_text()
                except:
                    print('ID:' + str(_id) + 'all_in_span[7]')
                    continue

                try:
                    _publishers = all_in_span[8].get_text()
                except:
                    print('ID:' + str(_id) + 'all_in_span[8]')
                    continue

        current_index += 3

        # print(_id, _game, _treleasedate, _developers, _publishers)
        genre_config_df = genre_config_df.append([{'ID': _id, 'Game': _game, 'ReleaseDate': _treleasedate,
                                                   'Developer': _developers, 'Publisher': _publishers}],
                                                 ignore_index=True)
        _count += 1

    genre_config_df.to_csv(output_file)
    print('count:  ' + str(_count))
