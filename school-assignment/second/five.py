import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from scipy import stats

# set the ply font to display Chinese
matplotlib.rc('font', family='Microsoft YaHei')

# get the abs path of data file
path = os.path.dirname(__file__)
path = path + "\\..\\..\\data\\data_second.xlsx"

# read the data of first problem
df1 = pd.read_excel(path, "跑步数据")

# plt.hist(df1.time)


# sns.distplot(df1.time)

# print(stats.kstest(df1.time, cdf='norm'))
# print(stats.shapiro(df1.time))

# plt.show()


t, pp = stats.ttest_1samp(df1.time, 103.5)
p = pp/2
print('t = ',t,', p = ', p)