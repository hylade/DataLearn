import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 45, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)

# print(df)
# print(df.head()) # 输出除最后 1 行
# print(df.tail()) # 输出除第 1 行
# print(df.tail(2)) # 输出后面 2 行

# print(df.set_index('Day')) # 将 Day 作为索引
# df.set_index('Day', inplace=True) # 当 inplace 设置为 True 时，将不会返回新 DataFrame ，而是直接修改
# print(df.head())

# print(df['Visitors'])
# print(df.Visitors) # 当属性中间存在空格时，只能使用第一种方法

#print(df[['Bounce_Rate', 'Visitors']]) # 输出多列的时候要加双 []

print(df.Visitors.tolist())
print(np.array(df[['Bounce_Rate', 'Visitors']]))

df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df2)