import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

## 避免输出省略
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

## 读取数据
df = pd.read_csv('iris-data.csv')

print(df.head()) # head() 默认输出 5 行
print(df.describe()) # 输出 df 数据信息
print(df.info())

## 删除缺失信息行
df = df.dropna(subset=['petal_width_cm']) # subset 用于确定在哪几列进行缺失信息
print(df.info())