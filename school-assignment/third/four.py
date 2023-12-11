import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_squared_error


# get the data file path
file_path = Path(__file__).parent / "../../data/data_third.xlsx"

# read the data file
data = pd.read_excel(file_path, '体脂率数据')

y = data['brozek']
x = data[['age', 'weight', 'height', 'adipos', 'neck', 'chest', 'abdom', \
          'hip', 'thigh', 'knee', 'ankle', 'biceps', 'forearm', 'wrist']]

linear_model = LinearRegression()
lasso_model = Lasso(alpha=1)

linear_model.fit(x, y)
lasso_model.fit(x, y)

predict_l = linear_model.predict(x)
predict_la = lasso_model.predict(x)

mse_l = mean_squared_error(y, predict_l)
mse_la = mean_squared_error(y, predict_la)

print('linear')
print('coef', linear_model.coef_)
print('const', linear_model.intercept_)
print('mse', mse_l)

print('lasso')
print('coef', lasso_model.coef_)
print('const', lasso_model.intercept_)
print('mse', mse_la)