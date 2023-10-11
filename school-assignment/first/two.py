# this is the code of first problem of first task
# written by zhaopiaoyang

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# set the ply font to display Chinese
matplotlib.rc('font', family='Microsoft YaHei')

# get the abs path of data file
path = os.path.dirname(__file__)
path = path + "\\..\\..\\data\\data_one.xlsx"

# read the data of the second problem
df1 = pd.read_excel(path, "two", index_col=None)

# drop the second row
df1 = df1.set_index(df1['school'])
data = df1.drop(columns='school')

data = pd.DataFrame(df1)

labels = data.index
x = np.arange(len(labels))
width = 0.3


# fig, ax = plt.subplots()

# ax.bar(x-0.15, data['money'], width=0.3, color='blue', label='财政拨款')
# ax.bar(x+0.15, data['income'], width=0.3, color='yellow', label='总收入')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)

# ax2 = ax.twinx()
# ax2.scatter(x, data['percent'], s=10, label='财政拨款占比', color='red')
# ax2.plot(x, data['percent'], color='red')
# fig.legend()

# plt.show()


# sns.regplot(x = 'money', y ='income', data= data)
# plt.show()


# sns.regplot(x = 'te', y ='per te', data= data)
# sns.regplot(x = 'st', y ='per st', data= data)
# plt.show()

fig, ax = plt.subplots()
ax.bar(x, data['te']*data['per te'])
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.show()