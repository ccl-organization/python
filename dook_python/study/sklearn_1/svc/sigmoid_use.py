# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# @Author: appleyuchi
# @Date:   2018-12-15 20:35:43
# @Last Modified by:   appleyuchi
# @Last Modified time: 2018-12-17 19:57:28

from study.sklearn_1 import datasets
from plot import *

from study.sklearn_1 import PolynomialFeatures, StandardScaler
from study.sklearn_1 import SVC
from study.sklearn_1 import Pipeline

X, y = datasets.make_moons(noise=0.15, random_state=666)
# plt.scatter(X[y==0, 0], X[y==0, 1])
# plt.scatter(X[y==1, 0], X[y==1, 1])
# plt.show()
print"X=",X
print len(X)
print"y=",y
print len(y)
degree=10
poly = PolynomialFeatures(degree)
transform_X=poly.fit_transform(X)
print"transform_X=",transform_X


# print dir(sklearn_1.svm)
def PolynomialSVC(degree, C=5):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        # ('linearSVC', LinearSVC(C=C))#注意这两句都行
        ('kernelSVC', SVC(kernel='sigmoid', degree=degree, C=C,class_weight={0:80,1:80})
        )#注意这两句都行
    ])

poly_svc = PolynomialSVC(degree=10)
poly_svc.fit(X, y)

plot_decision_boundary(poly_svc, axis=[-1.5, 2.5, -1.0, 1.5])
plt.scatter(X[y==0, 0], X[y==0, 1])
plt.scatter(X[y==1, 0], X[y==1, 1])
plt.show()