# -*- coding: UTF-8 -*-

from study.sklearn_1 import linear_model
# import sklearn_1
# 普通最小二乘法
reg = linear_model.LinearRegression()
reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
s=reg.coef_

# 岭回归的复杂度
reg = linear_model.Ridge (alpha = .5)
reg.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
s=reg.coef_
s1=reg.intercept_


reg = linear_model.Lasso(alpha = 0.1)
s1=reg.fit([[0, 0], [1, 1]], [0, 1])
s2=reg.predict([[1, 1]])

from study.sklearn_1 import KDTree
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
kdt = KDTree(X, leaf_size=30, metric='euclidean')
s1=kdt.query(X, k=2, return_distance=False)

print  ''



