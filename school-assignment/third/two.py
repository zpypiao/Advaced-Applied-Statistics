import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import seaborn as sns

# get the data file path
file_path = Path(__file__).parent / "../../data/data_third.xlsx"

# read the data file
data = pd.read_excel(file_path, '电池数据', skiprows=0)

data.columns = ['z1', 'z2', 'z3', 'z4', 'z5', 'y']

# data = (data - data.mean())/data.std()

data['y'] = np.log(data['y'])



# data['z6'] = data['z2'] * data['z4']
# data['z7'] = data['z2'] * data['z5']
# data['z8'] = data['z4'] * data['z5']


x = data.drop('y', axis=1)
x = x.drop('z3', axis=1)
x = x.drop('z1', axis=1)
# x = x.drop('z4', axis=1)
y = data['y']

# add the constant column
x_new = sm.add_constant(x)

model = sm.OLS(y, x_new)
results = model.fit()



sse = results.ssr
sst = results.centered_tss
ssr = sst - sse

print("回归平方和 (SSR):", ssr)
print("残差平方和 (SSE):", sse)
print("总平方和 (SST):", sst)

print(results.summary())

# formula = 'life ~ charge_rate + discharge_rate + discharge_depth + tem + voltage'
# formula = 'y ~  z1 + z2 + z3 + z4  + z5'
# model = ols(formula, data=data)
# results = model.fit()

# print(results.summary())

standardized_residuals = results.get_influence().resid_studentized_internal
plt.scatter(results.fittedvalues, standardized_residuals, alpha=0.7)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.xlabel('Fitted Values')
plt.ylabel('Standardized Residuals')
plt.title('Standardized Residuals vs Fitted Values')
plt.show()


residuals = results.resid

# 绘制残差直方图
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
sns.histplot(residuals, kde=True, bins=20)
plt.title('Residuals Histogram')
plt.xlabel('Residuals')
plt.ylabel('Frequency')

# 绘制残差正态图
plt.subplot(1, 2, 2)
sm.qqplot(residuals, line='s')
plt.title('Q-Q Plot of Residuals')

plt.tight_layout()
plt.show()
