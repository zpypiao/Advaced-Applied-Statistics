import numpy as np
import pandas as pd
from pathlib import Path
from scipy.stats import kstest
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# get the data file path
file_path = Path(__file__).parent / "../data/test.xlsx"

# read the data file
data = pd.read_excel(file_path, 'Sheet3')

result_dict = {}


for each in data.columns:
    if '64' in each:
        result_dict[each] = kstest(data.loc[:63,each],cdf = "norm")
    else:    
        result_dict[each] = kstest(data.loc[:,each],cdf = "norm")

for i in range(1, 5):
    plt.subplot(2, 2, i)
    each = data.columns[i-1]
    if '64' in each:
        sns.distplot(data.loc[:63,each], kde=False, fit=stats.norm)
    else:
        sns.distplot(data.loc[:,each], kde=False, fit=stats.norm)
    plt.title(str('KS='+str(result_dict[each][0])+',pV:'+str(result_dict[each][1])))
plt.show()



for each in result_dict:
    print(each, result_dict[each])