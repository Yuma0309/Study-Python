import pandas
df0 = pandas.read_csv(
    'chap6_data.csv', encoding='utf-8')
col_point = df0['point']
print(col_point.mean())