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