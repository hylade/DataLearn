import numpy as np
import pandas as pd

dataset = pd.read_csv('Data.csv') # 读取 csv 文件
X = dataset.iloc[:, : -1].values # .iloc[行, 列]
# 此处 -1 指倒数第二列
Y = dataset.iloc[:, 3].values
# 此处 3 为第四列，即倒数第一列

## 处理丢失数据
## 下述代码使用数组 X 去“训练”一个Imputer类，然后用该类的对象去处理数组 X 中的缺失值
from sklearn.preprocessing import Imputer
# 用平均值代替缺失值， axis = 0 表示按列进行
imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)
# imputer.fit(X[:, 需要补全的列]) ，这里的列编号从 1 开始
imputer = imputer.fit(X[:, 1: 3])
X[:, 1: 3] = imputer.transform(X[:, 1: 3])

# 解析分类数据
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# LabelEncoder 是用来对分类型特征值进行编码，即对不连续的数值或文本进行编码
# fit_transform(y) 相当于先进行 fit 再进行 transform ，即把 y 塞到字典中去以后再进行 transform 得到索引值
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

# 创建虚拟变量
onehotencoder = OneHotEncoder(categorical_features = [0]) # 说明对第一列编码
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
print(X)
## 拆分数据集为训练集合和测试集合
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
# 随机数种子，保证重复试验时得到的测试集合相同

## 特征量化
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
# 为使各特征的均值为 0 ，方差为 1
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)