from fintel import data, utils

shorts_df = data.get_shorts()
ownership_df = data.get_ownership()

sql = utils.SQLDB(source='fintel')
sql.load_sql(df=shorts_df, table_name='shorts')
sql.load_sql(df=ownership_df, table_name='ownership')

sql.disconnect()
print('ok')
