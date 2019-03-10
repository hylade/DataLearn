## 导入库
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## 导入数据集
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]]
Y = dataset.iloc[:, 4]

## 将数据集分为训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

## 特征缩放
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# fit_transform 先拟合数据，再标准化
X_train = sc.fit_transform(X_train)
# transform 数据标准化
X_test = sc.transform(X_test)
# fit(x) 传一个参数的是无监督学习的算法
# transform（）和 fit_transform（）的运行结果是一样的
# 但运行结果一模一样不代表这两个函数可以互相替换，绝对不可以
# transform函数是一定可以替换为fit_transform函数的，fit_transform函数不能替换为transform函数
# 使用不同函数原因参照 https://www.cnblogs.com/keye/p/8875128.html

## 将逻辑回归应用于训练集
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

## 预测
## 预测测试集结果
y_pred = classifier.predict(X_test)

## 评估预测
# 预测测试集后，将评估逻辑回归模型是否正确的学习和理解，故存在混淆矩阵包含模型正确和错误的预测

## 生成混淆矩阵
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_pred)

## 可视化
from matplotlib.colors import ListedColormap
X_set, Y_set = X_train, Y_train
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min()-1, stop=X_set[:, 0].max()+1, step=0.01),
                     np.arange(start=X_set[:, 1].min()-1, stop=X_set[:, 1].max()+1, step=0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('red', 'green')))
# arange() 用于创建等差数列
# contourf 用于绘制三维等高线，且会对等高线间的区域进行填充
# ravel 用于将多维数组转换为以为数组，且一般不会产生原数据的副本
# alpha 用于调整图像透明度

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max()) # 设置坐标轴刻度范围

for i, j in enumerate(np.unique(Y_set)):
    plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label=j)

plt.title('Logistic(Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

X_set, Y_set = X_test, Y_test
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min()-1, stop=X_set[:, 0].max()+1, step=0.01),
                     np.arange(start=X_set[:, 1].min()-1, stop=X_set[:, 1].max()+1, step=0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('red', 'green')))

plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i, j in enumerate(np.unique(Y_set)):
    plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label=j)

plt.title('Logistic(Test Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()