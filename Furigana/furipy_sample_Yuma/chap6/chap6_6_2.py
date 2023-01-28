import pandas
import matplotlib.pyplot as plt
df0 = pandas.read_csv('chap6_data.csv', encoding='utf-8')
col_sex = df0['sex']
col_point = df0['point']
col_point.hist(by=col_sex, bins=6, range=(-0.5, 5.5))
plt.savefig('chap6_hist.png')