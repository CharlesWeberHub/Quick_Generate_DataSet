import json
import time
import pandas as pd

_666_games_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/data/out_put_final/final_new_form(6_months_split_discount).xls'
_666_games_df = pd.read_excel(_666_games_path)

time_list = ['2019-05-01 08:00:00', '2019-06-01 08:00:00', '2019-07-01 08:00:00', '2019-08-01 08:00:00',
             '2019-09-01 08:00:00', '2019-10-01 08:00:00']

t1_stamp = int(time.mktime(time.strptime(time_list[0], "%Y-%m-%d %H:%M:%S")))
t2_stamp = int(time.mktime(time.strptime(time_list[1], "%Y-%m-%d %H:%M:%S")))
t3_stamp = int(time.mktime(time.strptime(time_list[2], "%Y-%m-%d %H:%M:%S")))
t4_stamp = int(time.mktime(time.strptime(time_list[3], "%Y-%m-%d %H:%M:%S")))
t5_stamp = int(time.mktime(time.strptime(time_list[4], "%Y-%m-%d %H:%M:%S")))
t6_stamp = int(time.mktime(time.strptime(time_list[5], "%Y-%m-%d %H:%M:%S")))

id_p_n = pd.DataFrame(columns=['ID', 'positive_count', 'negative_count'])

print(t1_stamp)
print(t2_stamp)
print(t3_stamp)
print(t4_stamp)
print(t5_stamp)
print(t6_stamp)

# timeStamp = 1488326400
# localTime = time.localtime(timeStamp)
# strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
# print(strTime)
now_ID = 0

for index, row in _666_games_df[['QueryID']].iterrows():
    # print(row['QueryID'])
    if now_ID != row['QueryID']:
        now_ID = row['QueryID']

        filename = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/time_p_n_json/' + str(now_ID) + '.json'
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        slot_list = data['results']['rollups']

        # print(slot_list)

        _ski = 0
        is_start = False

        ind_1 = None
        ind_2 = None
        ind_3 = None
        ind_4 = None
        ind_5 = None
        ind_6 = None

        slo_index = 0

        for _tt in slot_list:
            if _tt['date'] == t1_stamp:
                ind_1 = slo_index

            if _tt['date'] == t2_stamp:
                ind_2 = slo_index

            if _tt['date'] == t3_stamp:
                ind_3 = slo_index

            if _tt['date'] == t4_stamp:
                ind_4 = slo_index

            if _tt['date'] == t5_stamp:
                ind_5 = slo_index

            if _tt['date'] == t6_stamp:
                ind_6 = slo_index

            slo_index += 1

        if ind_1 is None:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': '','negative_count': ''}, ignore_index=True)
        else:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': str(slot_list[ind_1]['recommendations_up']),'negative_count': str(slot_list[ind_1]['recommendations_down'])}, ignore_index=True)

        if ind_2 is None:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': '','negative_count': ''}, ignore_index=True)
        else:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': str(slot_list[ind_2]['recommendations_up']),'negative_count': str(slot_list[ind_2]['recommendations_down'])}, ignore_index=True)

        if ind_3 is None:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': '','negative_count': ''}, ignore_index=True)
        else:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': str(slot_list[ind_3]['recommendations_up']),'negative_count': str(slot_list[ind_3]['recommendations_down'])}, ignore_index=True)

        if ind_4 is None:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': '','negative_count': ''}, ignore_index=True)
        else:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': str(slot_list[ind_4]['recommendations_up']),
                                    'negative_count': str(slot_list[ind_4]['recommendations_down'])}, ignore_index=True)

        if ind_5 is None:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': '','negative_count': ''}, ignore_index=True)
        else:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': str(slot_list[ind_5]['recommendations_up']),
                                    'negative_count': str(slot_list[ind_5]['recommendations_down'])}, ignore_index=True)

        if ind_6 is None:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': '','negative_count': ''}, ignore_index=True)
        else:
            id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': str(slot_list[ind_6]['recommendations_up']),
                                    'negative_count': str(slot_list[ind_6]['recommendations_down'])}, ignore_index=True)

# id_p_n = id_p_n.convert_objects(convert_numeric=True)
print(id_p_n.info())

id_p_n.to_excel('C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/p_n_stamp.xls')


        # for _tt in slot_list:
        #     if _ski >= 6:
        #         break
        #
        #     if _tt['date'] == t1_stamp:
        #         is_start = True
        #
        #     if is_start:
        #         # print('t_stamp: ' + str(_tt['date']))
        #         # print('t_recom_up: ' + str(_tt['recommendations_up']))
        #         # print('t_recom_down: ' + str(_tt['recommendations_down']))
        #         id_p_n = id_p_n.append({'ID': now_ID, 'positive_count': str(_tt['recommendations_up']),
        #                                 'negative_count': str(_tt['recommendations_down'])}, ignore_index=True)
        #         _ski += 1
        # break
# id_p_n.to_excel('p_n_stamp.xls')

# if _tt['date']==t1_stamp:
#     print('t1_stamp: '+str(_tt['date']))
#
# if _tt['date']==t2_stamp:
#     print('t2_stamp: '+str(_tt['date']))
#
# if _tt['date']==t3_stamp:
#     print('t3_stamp: '+str(_tt['date']))
#
# if _tt['date']==t4_stamp:
#     print('t4_stamp: '+str(_tt['date']))
#
# if _tt['date']==t5_stamp:
#     print('t5_stamp: '+str(_tt['date']))
#
# if _tt['date']==t6_stamp:
#     print('t6_stamp: '+str(_tt['date']))

# print(data['results']['start_date'])
# print(data['results']['end_date'])
#
# start_Time = time.localtime(data['results']['start_date'])
# st_Time = time.strftime("%Y-%m-%d %H:%M:%S", start_Time)
# print(st_Time)
#
# end_Time = time.localtime(data['results']['end_date'])
# ed_Time = time.strftime("%Y-%m-%d %H:%M:%S", end_Time)
# print(ed_Time)
