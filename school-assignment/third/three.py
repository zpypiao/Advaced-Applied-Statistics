import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import statsmodels.api as sm
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from statsmodels.multivariate.manova import MANOVA

# get the data file path
file_path = Path(__file__).parent / "../../data/data_third.xlsx"

# read the data file
data = pd.read_excel(file_path, '破产企业与财务状况良好企业经营数据', skiprows=0)

data.columns = ['v1', 'v2', 'v3', 'v4', 'attr']





def logit():
    y = data['attr']
    x = sm.add_constant(data[['v1', 'v2', 'v3', 'v4']])

    model = sm.Logit(y, x)
    result = model.fit()

    print(result.summary())



    pry = result.predict(x)

    pry = np.round(np.array(pry))

    print(pry, y)
    accuracy = accuracy_score(y, pry)

    print('the accuracy of the logit model is', accuracy)


def figure():
    data_1 = data[data['attr'] == 1]
    data_2 = data[data['attr'] == 0]

    plt.plot(data_1.drop('attr', axis=1).mean(), 'red', label='brup')
    plt.plot(data_2.drop('attr', axis=1).mean(), 'green', label='np-brup')
    plt.legend()
    plt.title('Contour drawing')
    plt.show()



def lllogit():
    y = data['attr']
    x = sm.add_constant(data[['v1', 'v2', 'v3', 'v4']])
    log = LogisticRegression()
    log.fit(x, y)

    yp = log.predict(x)

    conf_matrix = metrics.confusion_matrix(y, yp)

# 提取混淆矩阵中的元素
    TP, TN, FP, FN = conf_matrix.ravel()

    # 计算准确率
    accuracy = (TP + TN) / (TP + TN + FP + FN)

    # 打印准确率
    print("Accuracy:", accuracy)

logit()

data = sm.add_constant(data)


manova = MANOVA.from_formula('v1 + v2 + v3 + v4 ~ attr', data=data)

print(manova.mv_test().summary())