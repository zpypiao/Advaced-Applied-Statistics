# this is the code of first problem of first task
# written by zhaopiaoyang

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
path = path + "\\..\\..\\data\\data_one.xlsx"

# read the data of first problem
df1 = pd.read_excel(path, "three", index_col='地区')

view = df1.describe()

view.loc['R'] = view.loc['max'] - view.loc['min']
view.loc['COV'] = view.loc['std']/view.loc['mean']
view.loc['VAR'] = df1.var()


# view.to_excel('out1.xlsx', sheet_name='sheet1')
# print(view)

# print(df1)

outin = df1.columns

oucome = []

ave = pd.DataFrame({'人均GDP':[6212.01], '三产比重':[32.87], '人均消费':[2972], '人口增长':[9.5]})

for each in outin:
    t, p_twoTail = stats.ttest_1samp(df1[each], ave[each])
    p_oneTail = p_twoTail/2
    oucome.append([each, t, p_oneTail, p_twoTail])

outcome = pd.DataFrame(oucome, columns=['name', 't', 'p_oneTail', 'p_twoTail'])

outcome.to_excel('p.xlsx', sheet_name='sheet1')