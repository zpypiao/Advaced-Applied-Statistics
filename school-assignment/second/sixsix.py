import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from scipy import stats
from pingouin import multivariate_normality

# set the ply font to display Chinese
matplotlib.rc('font', family='Microsoft YaHei')

# get the abs path of data file
path = os.path.dirname(__file__)
path = path + "\\..\\..\\data\\data_second.xlsx"

# read the data of first problem
data = pd.read_excel(path, "居民消费支出数据", skiprows=1, index_col='地区')
data.columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']

# the basic describe of the data
# view = data.describe()

# with pd.ExcelWriter('sec_six.xlsx') as writer:
#     view.to_excel(writer, sheet_name='describe')
# the cov of the data
#     data.corr().to_excel(writer, sheet_name='cov')


for each in data.columns:
    print(each, stats.kstest(data[each], cdf='norm'), stats.shapiro(data[each]))


# mean_data = np.mean(data, axis=0)

# cov_data = np.cov(data.T)

# h, p, n = multivariate_normality(data, 0.05)


# print(' The Henze-Zirkler test statistic=', h, ' P-value=',p, 'normal', n)

# ax1 = plt.subplot(2, 4, 1)
# sns.distplot(data.x1)
# ax1.set_title('食品')

# ax2 = plt.subplot(2, 4, 2)
# sns.distplot(data.x2)
# ax2.set_title('衣着')

# ax3 = plt.subplot(2, 4, 3)
# sns.distplot(data.x3)
# ax3.set_title('居住')

# ax4 = plt.subplot(2, 4, 4)
# sns.distplot(data.x4)
# ax4.set_title('家庭用品')

# ax5 = plt.subplot(2, 4, 5)
# sns.distplot(data.x5)
# ax5.set_title('医疗')

# ax6 = plt.subplot(2, 4, 6)
# sns.distplot(data.x6)
# ax6.set_title('交通')

# ax7 = plt.subplot(2, 4, 7)
# sns.distplot(data.x7)
# ax7.set_title('教育')

# ax8 = plt.subplot(2, 4, 8)
# sns.distplot(data.x8)
# ax8.set_title('杂项')

# plt.show()


data_n = data.loc[data.x9 == 1]
data_e = data.loc[data.x9 == 2]
data_s = data.loc[data.x9 == 3]
data_w = data.loc[data.x9 == 4]

drop_col = ['x1', 'x5', 'x6', 'x7', 'x8', 'x9']

data_n.drop(columns=drop_col, inplace=True)
data_e.drop(columns=drop_col, inplace=True)
data_s.drop(columns=drop_col, inplace=True)
data_w.drop(columns=drop_col, inplace=True)

set_columns = ['衣着', '居住', '家庭用具']
data_n.columns = set_columns
data_e.columns = set_columns
data_s.columns = set_columns
data_w.columns = set_columns

re = []

f, p = stats.f_oneway(data_n, data_e, data_s, data_w)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'nesw'])

f, p = stats.f_oneway(data_e, data_s, data_w)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'esw'])

f, p = stats.f_oneway(data_n, data_s, data_w)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'nsw'])

f, p = stats.f_oneway(data_n, data_e, data_w)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'new'])

f, p = stats.f_oneway(data_n, data_e, data_s)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'nes'])


f, p = stats.f_oneway(data_n, data_e)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'ne'])

f, p = stats.f_oneway(data_n, data_s)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'ns'])

f, p = stats.f_oneway(data_n, data_w)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'nw'])

f, p = stats.f_oneway(data_e, data_s)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'es'])

f, p = stats.f_oneway(data_e, data_w)
re.append([f[0], f[1], f[2], p[0], p[1], p[2], 'sw'])

result = pd.DataFrame(re)

result.to_excel('sixsix.xlsx', sheet_name='sheet1')