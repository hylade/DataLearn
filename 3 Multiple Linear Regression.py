## 导入库
import pandas as pd
import numpy as np

## 导入数据库
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values

## 类别数据数字化
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3]) # 对第三列进行编码
X = onehotencoder.fit_transform(X).toarray()

## 躲避虚拟变量陷阱
# 通过减少一个分类变量从而避免
X = X[:, 1:]

## 拆分数据集为训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

## 在训练集上训练多元线性回归模型
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

## 在测试集上预测结果
y_pred = regressor.predict(X_test)