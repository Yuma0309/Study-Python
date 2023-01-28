import pandas
df0 = pandas.read_csv(
    'chap6_data.csv', encoding='utf-8')
col_sex = df0['sex']
col_point_m = df0.loc[col_sex == 'M', 'point']
col_point_f = df0.loc[col_sex == 'F', 'point']
mode_m = col_point_m.mode()
mode_f = col_point_f.mode()
print('男性')
print(mode_m)
print('女性')
print(mode_f)