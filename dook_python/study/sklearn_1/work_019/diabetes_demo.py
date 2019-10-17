# -*- coding: UTF-8 -*-

import numpy as np
from study.sklearn_1 import datasets

diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test  = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test  = diabetes.target[-20:]
print  diabetes_X_train
print 11111
print diabetes_y_train
from study.sklearn_1 import linear_model
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print(regr.coef_)
# [   0.30349955 -237.63931533  510.53060544  327.73698041 -814.13170937
#  492.81458798  102.84845219  184.60648906  743.51961675   76.09517222]

# 均方误差
s1=np.mean((regr.predict(diabetes_X_test)-diabetes_y_test)**2)
# 2004.56760268...

# 方差分数：1 是完美的预测
# 0 意味着 X 和 y 之间没有线性关系。
s2=regr.score(diabetes_X_test, diabetes_y_test)
# 0.5850753022690...

X = np.c_[ .5, 1].T
y = [.5, 1]
test = np.c_[ 0, 2].T
regr = linear_model.LinearRegression()

import matplotlib.pyplot as plt 
plt.figure() 

np.random.seed(0)
for _ in range(6): 
   this_X = .1*np.random.normal(size=(2, 1)) + X
   regr.fit(this_X, y)
   plt.plot(test, regr.predict(test))
   plt.scatter(this_X, y, s=3)



regr = linear_model.Ridge(alpha=.1)

plt.figure() 

np.random.seed(0)
for _ in range(6): 
     this_X = .1*np.random.normal(size=(2, 1)) + X
     regr.fit(this_X, y)
     plt.plot(test, regr.predict(test))
     plt.scatter(this_X, y, s=3)
print