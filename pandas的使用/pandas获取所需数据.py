import pandas as pd
from sqlalchemy import create_engine


def download_data_from_db(sql):
    """
    read/load data from database

    input:
    dataframe: pandas DataFrame
    sql: the sql query used to extract data from MySQL
    schema_name: the schema data stored

    output:
    True/False
    """

    try:
        schema_name = 'account_management_system_test',
        # schema_name = 'account_management_system',
        cnx = create_engine(
            # 'mysql+pymysql://web:WebToT123@60.191.40.238:8060/%s?charset=utf8' %
            'mysql+pymysql://root:yjn123@192.168.110.128:3306/%s?charset=utf8' %
            schema_name, encoding="utf-8", echo=False)
        df = pd.read_sql(sql, con=cnx)
        return df
    except Exception as e:
        return False


# a_sql = "select * from ticker_fund_record where date between '2020-12-20' and '2020-12-22';"
# df1 = download_data_from_db(a_sql)
# df1['date'] = df1['date'].apply(lambda x: x.__format__("%Y-%m-%d"))
# df2 = df1[(df1['product_id'] == 4)]
# print(df2.date.tolist())
# df2 = df2[(df2['date'] == '2020-12-21')]
# print(df2)


def download_ticker_data_from_db(sql):
    """
    read/load data from database

    input:
    sql: the sql query used to extract data from MySQL
    schema_name: the schema data stored

    output:
    sql excacution result
    output as pandas DataFrame

    """
    # create connection with DB

    schema_name = 'daily_data'
    cnx = create_engine(
        'mysql+pymysql://web:WebToT123@60.12.233.50:3000/%s?charset=utf8' %
        schema_name, encoding="utf-8", echo=False)
    df = pd.read_sql(sql, con=cnx)
    return df


trader_list_sql = "select DISTINCT TRADE_DAYS from ASHARECALENDAR order by TRADE_DAYS"
trader_df = download_ticker_data_from_db(trader_list_sql)
trader_df['TRADE_DAYS'] = trader_df['TRADE_DAYS'].apply(lambda x: x[0:4] + '-' + x[4:6] + '-' + x[6:])
trader_list = trader_df['TRADE_DAYS'].tolist()
today = '2021-01-19'
date_index = trader_list.index(today)
next_day = trader_list[(date_index + 1)]
last_day = trader_list[(date_index - 1)]
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
sql1 = "select * from ticker_fund_record where date between '%s' and '%s'" % (last_day, next_day)
sql2 = "select * from futures_fund_record where date between '%s' and '%s'" % (last_day, next_day)
fund_assets_df = download_data_from_db(sql1)
futures_assets_df = download_data_from_db(sql2)
print(fund_assets_df)
fund_assets_df['date'] = fund_assets_df['date'].apply(lambda x: x.__format__("%Y-%m-%d"))
futures_assets_df['date'] = futures_assets_df['date'].apply(lambda x: x.__format__("%Y-%m-%d"))

product_id = 21
last_fund_assets_df = fund_assets_df[
    (fund_assets_df['product_id'] == product_id) & (fund_assets_df['date'] == last_day)]
last_futures_assets_df = futures_assets_df[
    (futures_assets_df['product_id'] == product_id) & (futures_assets_df['date'] == last_day)]
# 上一天
ticker_amount_last = last_fund_assets_df['securities_assets'].sum()  # 证券求和
ticker_transfer_in_out_last = last_fund_assets_df['transfer_in_out'].sum()  # 证券转入转出
futures_amount_last = last_futures_assets_df['futures_assets'].sum()  # 期货求和
futures_transfer_in_out_last = last_futures_assets_df['transfer_in_out'].sum()  # 期货转入转出
total_amount_last = ticker_amount_last + futures_amount_last
total_transfer_in_out = ticker_transfer_in_out_last + futures_transfer_in_out_last

# 当天
today_fund_assets_df = fund_assets_df[(fund_assets_df['product_id'] == product_id) & (fund_assets_df['date'] == today)]
today_futures_assets_df = futures_assets_df[
    (futures_assets_df['product_id'] == product_id) & (futures_assets_df['date'] == today)]
ticker_amount_today = today_fund_assets_df['securities_assets'].sum()  # 证券求和
ticker_transfer_in_out_today = today_fund_assets_df['transfer_in_out'].sum()  # 证券转入转出

futures_amount_today = today_futures_assets_df['futures_assets'].sum()  # 期货求和
futures_transfer_in_out_today = today_futures_assets_df['transfer_in_out'].sum()  # 期货转入转出
total_amount_today = ticker_amount_today + futures_amount_today
total_transfer_in_today = ticker_transfer_in_out_today + futures_transfer_in_out_today

# 下一天
next_fund_assets_df = fund_assets_df[(fund_assets_df['product_id'] == product_id) & (fund_assets_df['date'] == next)]
next_futures_assets_df = futures_assets_df[
    (futures_assets_df['product_id'] == product_id) & (futures_assets_df['date'] == next)]
ticker_amount_next = next_fund_assets_df['securities_assets'].sum()  # 证券求和
ticker_transfer_in_out_next = next_fund_assets_df['transfer_in_out'].sum()  # 证券转入转出

futures_amount_next = next_futures_assets_df['futures_assets'].sum()  # 期货求和
futures_transfer_in_out_next = next_futures_assets_df['transfer_in_out'].sum()  # 期货转入转出
total_amount_next = ticker_amount_next + futures_amount_next
total_transfer_in_next = ticker_transfer_in_out_next + futures_transfer_in_out_next

if (total_amount_last + total_transfer_in_today + total_transfer_in_next) == 0:
    benefit_rate = 0
else:
    benefit_rate = ((total_amount_today + total_transfer_in_next) / (
            total_amount_last + total_transfer_in_today + total_transfer_in_next)
                    ) - 1
    benefit_rate = round(benefit_rate * 100, 2)
print(benefit_rate)
