import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.multivariate.manova import MANOVA

# 示例数据
data = {
    'Group': ['A'] * 30 + ['B'] * 30 + ['C'] * 30,
    'Variable1': np.random.normal(0, 1, 90),
    'Variable2': np.random.normal(0, 1, 90),
    'Variable3': np.random.normal(0, 1, 90)
}

df = pd.DataFrame(data)

# 将组别变量转换为哑变量
df['Group'] = pd.Categorical(df['Group'])
df_dummies = pd.get_dummies(df['Group'], prefix='Group')
df = pd.concat([df, df_dummies], axis=1)

# 指定因变量和组别变量
endog = df[['Variable1', 'Variable2', 'Variable3']]
exog = sm.add_constant(df[['Group_B', 'Group_C']])

# 进行 MANOVA
manova = MANOVA(endog, exog)
print(manova.mv_test())