from scipy.stats import bartlett
from pingouin import box_m, multivariate_normality
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.spatial import distance
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score



# get the data file path
file_path = Path(__file__).parent / "../../data/data_third.xlsx"

# read the data file
data = pd.read_excel(file_path, '蛙鱼数据', skiprows=0)


# revalue the column index
data.columns = ['country', 'sex', 'water', 'sea']

sample = data.iloc[0].drop('country', axis=0)

data = data.drop(0, axis=0)



dat1 = data[data['country']==1].drop('country', axis=1)
dat2 = data[data['country']==2].drop('country', axis=1)

dat3 = data.drop('country', axis=1)


# 执行 Box's M Test
result = box_m(data=data, dvs=['sex', 'water', 'sea'], group='country', alpha=0.05)

# 输出结果
print(result)

cov_1 = np.cov(dat1, rowvar=False)
cov_2 = np.cov(dat2, rowvar=False)

me_1 = np.mean(dat1, axis=0)
me_2 = np.mean(dat2, axis=0)

d1 = distance.mahalanobis(sample, me_1, np.linalg.inv(cov_1))
d2 = distance.mahalanobis(sample, me_2, np.linalg.inv(cov_2))

print('the distance between sample and group1 is :', d1)
print('the distance between sample and group2 is :', d2)

# 贝叶斯判别模型
model = QuadraticDiscriminantAnalysis()

# fisher判别模型
model = LinearDiscriminantAnalysis()

model.fit(data[['sex', 'water', 'sea']], data['country'])

# print('weight')
# print(model.coef_)
# print('cnstant')
# print(model.intercept_)
# pre = model.predict([sample])


pre = model.predict(data[['sex', 'water', 'sea']])
accuracy = accuracy_score(data['country'], pre)

print('accuracy rate', accuracy)