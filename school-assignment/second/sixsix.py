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
data = pd.read_excel(path, "居民消费支出数据", skiprows=1, index_col='地区')
data.columns = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8']

# the basic describe of the data
# view = data.describe()

# with pd.ExcelWriter('sec_six.xlsx') as writer:
#     view.to_excel(writer, sheet_name='describe')
# the cov of the data
#     data.corr().to_excel(writer, sheet_name='cov')


for each in data.columns:
    print(each, stats.kstest(data[each], cdf='norm'), stats.shapiro(data[each]))


mean_data = np.mean(data, axis=0)

cov_data = np.cov(data.T)

md = stats.multivariate_normal(mean=mean_data, cov=cov_data)

t, p = md.fit(data).pvalue

print(t, p)

sns.distplot(data.x5)
plt.show()