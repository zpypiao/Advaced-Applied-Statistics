import os
import pandas as pd


dir = 'D:/Docunments/Course/Advanced_applied_statistics/class/compare/'

clas = ['优', '良', '中', '差']


dfs = []

for each in clas:
    dir_path = dir + each
    res = [i.split('.')[0].replace('+', '-') for i in os.listdir(dir_path)]
    
    print(res)
    code = [i.split('-')[0] for i in res]

    name = [i.split('-')[1] for i in res]

    dfs.append(pd.DataFrame({'学号':code, '姓名':name, '成绩':each}))

outcome = pd.DataFrame()

for each in dfs:
    outcome = pd.concat([outcome, each])


outcome.to_excel('D:/Desktop/out.xlsx')
