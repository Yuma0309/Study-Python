import pandas
df0 = pandas.read_csv(
    'chap6_data.csv', encoding='utf-8')
col_sex = df0['sex']
col_point_m = df0.loc[col_sex == 'M', 'point']
col_point_f = df0.loc[col_sex == 'F', 'point']
describe_m = col_point_m.describe()
describe_f = col_point_f.describe()
print('男性基本統計量')
print(describe_m)
print('女性基本統計量')
print(describe_f)