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
df1 = pd.read_excel(path, "国家公园的游客数和面积", index_col='国家公园')

df1.columns = ['square', 'num']

corr = np.corrcoef(df1["square"], df1["num"])

r, p = stats.pearsonr(df1["square"], df1["num"])
print(r, p)

# indexnames1 = df1[df1['num']>4].index
# indexnames2 = df1[df1['num']<2].index

# df1.drop(indexnames1, inplace=True)
# df1.drop(indexnames2, inplace=True)

df1.drop('大雾山', inplace=True)
df1.num *= 100
sns.regplot(x="square", y="num", data=df1)
plt.show()
r, p = stats.pearsonr(df1["square"], df1["num"])
print(r, p)

# sns.regplot(x="square", y="num", data=df1)
# plt.show()

# plt.scatter(df1["square"], df1["num"])

# plt.show()
