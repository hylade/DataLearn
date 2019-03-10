## 导入相关库
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## 导入数据集
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
Y = dataset.iloc[:, 4].values

## 将数据集划分为训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

## 特征缩放
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

## 使用 K-NN 对训练集数据进行训练
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
# metric 用于确定距离方式
# p 用于确定闵式距离次方数
# n_neighbors 用于确定计算邻居数量
classifier.fit(X_train, Y_train)

## 预测
y_pred = classifier.predict(X_test)

## 生成混淆矩阵
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)