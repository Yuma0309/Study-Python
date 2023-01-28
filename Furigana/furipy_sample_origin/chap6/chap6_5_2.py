import pandas
df0 = pandas.read_csv(
    'chap6_data.csv', encoding='utf-8')
col_sex = df0['sex']
col_point_m = df0.loc[col_sex == 'M', 'point']
col_point_f = df0.loc[col_sex == 'F', 'point']
describe_m = col_point_m.describe()
describe_m.name = 'male'
describe_f = col_point_f.describe()
describe_f.name = 'female'
describe = pandas.concat([describe_m, describe_f],
                         axis=1)
print(describe)
