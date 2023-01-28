import pandas
df0 = pandas.read_csv(
    'chap6_data.csv', encoding='utf-8')
col_point = df0['point']
print(f'平均値は{col_point.mean()}')
