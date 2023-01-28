import pandas
df0 = pandas.read_csv(
    'chap6_data.csv', encoding='utf-8')
col_sex = df0['sex']
df0.loc[col_sex == 'F', 'point'] = 5
print(df0)
