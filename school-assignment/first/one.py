# this is the code of first problem of first task
# written by zhaopiaoyang

import os
import pandas as pd

# get the abs path of data file
path = os.path.dirname(__file__)
path = path + "\\..\\..\\data\\data_one.xlsx"

# read the data of first problem
df1 = pd.read_excel(path, "one", index_col=None)

print(df1)