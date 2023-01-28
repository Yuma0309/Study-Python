import pandas
df0 = pandas.read_csv(
    'chap6_data.csv', encoding='utf-8')
col_sex = df0['sex']
col_point_m = df0.loc[col_sex == 'M', 'point']
col_point_f = df0.loc[col_sex == 'F', 'point']
mean_m = col_point_m.mean()
mean_f = col_point_f.mean()
print(f'男性平均：{mean_m}、女性平均：{mean_f}')
