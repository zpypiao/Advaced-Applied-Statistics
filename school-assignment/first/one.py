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

# read the data of first problem
df1 = pd.read_excel(path, "one", index_col=None)

# translate data to a table by using the default tag
data = pd.DataFrame(df1, columns=['company', 'X total sales', 'Y profit', 'Z assets'])
company = data['company']
data = data.set_index('company')

# describe the table
view = data.describe()

# add the range, cov and var column value
view.loc['R'] = view.loc['max'] - view.loc['min']
view.loc['COV'] = view.loc['std']/view.loc['mean']
view.loc['VAR'] = data.var()

# display the data and save it to an excel file
view.to_excel('out.xlsx', sheet_name='sheet1')
print(view)


# # creat the figure to describe the data distribute
# fig, ax = plt.subplots(3, 1, sharex=True)


# # add the three dimensions of the data
# labels = ['X total sales', 'Y profit', 'Z assets']
# print(view['Z assets']['25%'])
# for i in range(3):

#     # scatter the point
#     ax[i].scatter(data.index, data[labels[i]], s=10)

#     # plot the line picture
#     ax[i].plot(data.index, data[labels[i]])

#     # add the control lines
#     ax[i].axhline(view[labels[i]]['75%'], color='red', label='75%')
#     ax[i].axhline(view[labels[i]]['mean'], color='yellow', label='mean')
#     ax[i].axhline(view[labels[i]]['25%'], color='blue', label='25%')

#     # set the title of the subfig
#     ax[i].set_title(labels[i])

# # display the label of first figure
# ax[0].legend()


print(data)
print(data['X total sales'].dtype)
# plot the scatter picture
sns.regplot(x='X total sales', y='Y profit', data=data)
plt.grid(True)
plt.show()

# calculate the cov value
print(np.cov(data['X total sales'], data['Y profit']))