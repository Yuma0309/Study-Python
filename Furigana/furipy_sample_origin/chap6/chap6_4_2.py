import pandas
df0 = pandas.read_csv(
    'chap6_data.csv', encoding='utf-8')
col_sex = df0['sex']
df_m = df0.loc[col_sex == 'M']
df_f = df0.loc[col_sex == 'F']
mean_m = df_m['point'].mean()
mean_f = df_f['point'].mean()
print(f'男性平均：{mean_m}、女性平均：{mean_f}')
