import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import levene
import pingouin as pg
from statsmodels.multivariate.manova import MANOVA
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import multivariate_t, chi2
from sklearn.covariance import EmpiricalCovariance

# get the data file path
file_path = Path(__file__).parent / "../../data/data_third.xlsx"

# read the data file
data = pd.read_excel(file_path, '婚姻数据', skiprows=0)

# revalue the column index
data.columns = ['x1', 'x2', 'x3', 'x4', 'attr']

# devide the data differentiate from the sex
data_man = data[data['attr']==1].drop('attr', axis=1)
data_woman = data[data['attr']==2].drop('attr', axis=1)

# get the mean of each set
mean_data = [data_man.mean(axis=0)]
mean_data.append(data_woman.mean(axis=0))

# plot the analysis outcome separately
# plt.plot(mean_data[0])
# plt.title('the judge of husband to wife')
# plt.show()
# plt.plot(mean_data[1])
# plt.title('the judge of wife to husband')
# plt.show()


# plot the analysis outcome in one fugure
# plt.plot(mean_data[0], 'red', label='the judge of husband to wife')
# plt.plot(mean_data[1], 'blue', label='the judge of wife to husband')
# plt.grid(True)
# plt.legend()
# plt.show()


for each in ['x1', 'x2', 'x3', 'x4']:
    res = levene(data_man[each], data_woman[each], center='mean')

    print(res)

data = sm.add_constant(data)


manova = MANOVA.from_formula('x1 + x2 + x3 + x4 ~ attr', data=data)

print(manova.mv_test().summary())


model = ols('attr ~  x1 + x2 + x3 + x4', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(model.summary())

x = np.array(data[['x1', 'x2', 'x3', 'x4']])
y = np.array(data['attr'])

# 提取各组数据
group1_data = data_man
group2_data = data_woman

mean1 = data_man.mean()
mean2 = data_woman.mean()

# 计算协方差矩阵
covariance_estimator = EmpiricalCovariance()
covariance_estimator.fit(np.vstack([group1_data, group2_data]))

# 计算 Hotelling's T-squared 统计量
n = len(group1_data)
t_squared = n * np.dot(np.dot(mean1 - mean2, np.linalg.inv(covariance_estimator.covariance_)), mean1 - mean2)

# 计算 p 值
degrees_of_freedom = len(mean1)
p_value = 1 - chi2.cdf(t_squared, degrees_of_freedom)

# 打印结果
print("Hotelling's T-squared 统计量:", t_squared)
print("p值:", p_value)