import os
import pandas as pd

#month_6_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(6_months).csv'
#month_6_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(12_months).csv'
month_6_path = '/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(6_quarters).csv'
month_6_df = pd.read_csv(month_6_path,index_col=0)


def convert_currency(var):
    """
    convert the string number to a float

    """
    new_value = var.replace(",", "").replace("$", "").replace("(", "").replace(")", "")
    return float(new_value)

month_6_df['max_discounted_percent(%)']=month_6_df['Max discount'].str.split('%', 1).str[0]


month_6_df['max_discounted_price($)']=month_6_df['Max discount'].str.split('%', 1).str[1]
month_6_df['max_discounted_price($)']=month_6_df['max_discounted_price($)'].apply(convert_currency)

month_6_df['max_discounted_percent(%)']=month_6_df['max_discounted_percent(%)'].fillna(0)
month_6_df['max_discounted_percent(%)']=month_6_df['max_discounted_percent(%)'].convert_objects(convert_numeric=True)
month_6_df['discounted(boolean)']= month_6_df['max_discounted_percent(%)'] > 0

#month_6_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(6_months_split_discount).csv')
#month_6_df.to_csv('/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(12_months_split_discount).csv')
month_6_df.to_excel('/Users/charles/PycharmProjects/Games_Research/append_monthly_quarterly/new_form(6_quarters_split_discount).xls')

