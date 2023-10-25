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
data = pd.read_excel(path, "耳朵数据")

# ind = data[data["组别"]==1].index

# print(ind)

# df1 = data[data[data["组别"]==1].index]

df1 = data.loc[data['组别']==1]
df2 = data.loc[data['组别']==2]
df3 = data.loc[data['组别']==3]


print(df1, df2, df3)