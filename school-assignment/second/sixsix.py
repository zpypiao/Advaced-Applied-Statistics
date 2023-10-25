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


view = data.describe()

with pd.ExcelWriter('sec_six.xlsx') as writer:
    view.to_excel(writer, sheet_name='describe')
    data.corr().to_excel(writer, sheet_name='cov')