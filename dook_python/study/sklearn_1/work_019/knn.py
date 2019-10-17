# -*- coding: UTF-8 -*-
import numpy as np
from study.sklearn_1 import datasets
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
s1=np.unique(iris_y)
print
# array([0, 1, 2])

# 将鸢尾属植物数据集分解为训练集和测试集
# 随机排列，用于使分解的数据随机分布
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_y_test  = iris_y[indices[-10:]]
# 创建和拟合一个最近邻分类器
from study.sklearn_1 import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train) 
# KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
#  metric_params=None, n_jobs=1, n_neighbors=5, p=2,
#  weights='uniform')
s1=knn.predict(iris_X_test)
# array([1, 2, 1, 0, 0, 0, 2, 1, 2, 0])
s2=iris_y_test
# array([1, 1, 1, 0, 0, 0, 2, 1, 2, 0])
print