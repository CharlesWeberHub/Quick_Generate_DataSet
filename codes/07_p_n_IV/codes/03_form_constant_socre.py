import pandas as pd
import os

# m_u_score_xls_path = '/Users/charles/PycharmProjects/Scrap_Score/venv/codes/meta_user_score.xls'
# m_u_score_df = pd.read_excel(m_u_score_xls_path)
#
# m_u_score_df['num_ratings'] = m_u_score_df['num_ratings'].str.split(' ', 1).str[0]
#
# print(m_u_score_df.info())
#
# m_u_score_df = m_u_score_df.convert_objects(convert_numeric=True)
# print(m_u_score_df.info())
#
# m_u_score_df.to_excel('meta_user_score_01.xls')

fisrt_game_score_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/scores(498_games)_final.xls'
fisrt_game_score = pd.read_excel(fisrt_game_score_path, index_col=0)

game_score_path = 'C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games/temp/'
game_score_list = os.listdir(game_score_path)
id_results = pd.DataFrame(
    columns=['ID', 'meta_score', 'num_critic_reviews', 'user_score', 'num_ratings', 'critic_positive', 'critic_mixed',
             'critic_negative', 'user_positive', 'user_mixed', 'user_negative'])

for i in range(len(game_score_list)):
    score_df = pd.read_excel(game_score_path + game_score_list[i], index_col=0)
    fisrt_game_score = fisrt_game_score.append(score_df, ignore_index=True)

fisrt_game_score.to_excel('C:/Users/charles/PycharmProjects/Quick_Generate_DataSet/codes/07_p_n_IV/498_games'
                          '/total_meta_user_score.xls')
