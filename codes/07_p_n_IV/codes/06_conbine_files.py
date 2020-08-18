import pandas as pd

m_u_score_path = '/Users/charles/PycharmProjects/Scrap_Score/venv/codes/meta_user_score_01.xls'
p_n_num_path = '/Users/charles/PycharmProjects/Scrap_Score/venv/codes/p_n_stamp.xls'

m_u_score_df = pd.read_excel(m_u_score_path)
p_n_num_df = pd.read_excel(p_n_num_path)

id_results = pd.DataFrame(
    columns=['ID', 'positive_count', 'negative_count', 'meta_score', 'num_critic_reviews', 'user_score', 'num_ratings',
             'critic_positive', 'critic_mixed',
             'critic_negative', 'user_positive', 'user_mixed', 'user_negative'])

for index, row in p_n_num_df.iterrows():
    current_row = row
    double_match = m_u_score_df.loc[m_u_score_df['ID'] == row['ID']]

    if double_match.shape[0] == 1:
        current_row['meta_score'] = double_match['meta_score'].iloc[0]
        current_row['num_critic_reviews'] = double_match['num_critic_reviews'].iloc[0]
        current_row['user_score'] = double_match['user_score'].iloc[0]
        current_row['num_ratings'] = double_match['num_ratings'].iloc[0]
        current_row['critic_positive'] = double_match['critic_positive'].iloc[0]
        current_row['critic_mixed'] = double_match['critic_mixed'].iloc[0]
        current_row['critic_negative'] = double_match['critic_negative'].iloc[0]
        current_row['user_positive'] = double_match['user_positive'].iloc[0]
        current_row['user_mixed'] = double_match['user_mixed'].iloc[0]
        current_row['user_negative'] = double_match['user_negative'].iloc[0]

    else:
        current_row['meta_score'] = ''
        current_row['num_critic_reviews'] = ''
        current_row['user_score'] = ''
        current_row['num_ratings'] = ''
        current_row['critic_positive'] = ''
        current_row['critic_mixed'] = ''
        current_row['critic_negative'] = ''
        current_row['user_positive'] = ''
        current_row['user_mixed'] = ''
        current_row['user_negative'] = ''

    id_results = id_results.append(current_row)

    print('index')

id_results.to_csv('file_for_conbine.csv')
