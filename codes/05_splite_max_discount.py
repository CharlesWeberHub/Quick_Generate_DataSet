import os
import pandas as pd
import xlwt


month_6_path = r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\out_put_final\new_form(6_months).csv'
month_6_df = pd.read_csv(month_6_path, index_col=0)


def convert_currency(var):
    """
    convert the string number to a float

    """
    new_value = var.replace(",", "").replace("$", "").replace("(", "").replace(")", "")
    return float(new_value)


month_6_df['max_discounted_percent(%)'] = month_6_df['Max discount'].str.split('%', 1).str[0]

month_6_df['max_discounted_price($)'] = month_6_df['Max discount'].str.split('%', 1).str[1]
month_6_df['max_discounted_price($)'] = month_6_df['max_discounted_price($)'].apply(convert_currency)

month_6_df['max_discounted_percent(%)'] = month_6_df['max_discounted_percent(%)'].fillna(0)
month_6_df['max_discounted_percent(%)'] = pd.to_numeric(month_6_df['max_discounted_percent(%)'], errors='coerce')
# month_6_df['max_discounted_percent(%)'] = month_6_df['max_discounted_percent(%)'].convert_objects(convert_numeric=True)
month_6_df['discounted(boolean)'] = month_6_df['max_discounted_percent(%)'] > 0

month_6_df.to_excel(
    r'C:\Users\charles\PycharmProjects\Quick_Generate_DataSet\data\out_put_final\final_new_form(6_months_split_discount).xls')
