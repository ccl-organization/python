# -*- coding: UTF-8 -*-

from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer

X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

classif = OneVsRestClassifier(estimator=SVC(random_state=0))
s=classif.fit(X, y).predict(X)
# array([0, 0, 1, 1, 2])

y = LabelBinarizer().fit_transform(y)
s2=classif.fit(X, y).predict(X)

from sklearn.preprocessing import MultiLabelBinarizer
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
s2=classif.fit(X, y).predict(X)

from sklearn import datasets, svm
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target
svc = svm.SVC(C=1, kernel='linear')
s3=svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])

from sklearn.model_selection import KFold, cross_val_score
X = ["a", "a", "b", "c", "c", "c"]
k_fold = KFold(n_splits=3)
for train_indices, test_indices in k_fold.split(X):
     print('Train: %s | test: %s' % (train_indices, test_indices))
     
[svc.fit(X_digits[train], y_digits[train]).score(X_digits[test], y_digits[test])
         for train, test in k_fold.split(X_digits)]

cross_val_score(svc, X_digits, y_digits, cv=k_fold, n_jobs=-1)

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn import datasets, svm

digits = datasets.load_digits()
X = digits.data
y = digits.target

svc = svm.SVC(kernel='linear')
C_s = np.logspace(-10, 0, 10)



from sklearn import linear_model, datasets
lasso = linear_model.LassoCV()
diabetes = datasets.load_diabetes()
X_diabetes = diabetes.data
y_diabetes = diabetes.target
lasso.fit(X_diabetes, y_diabetes)
# LassoCV(alphas=None, copy_X=True, cv=None, eps=0.001, fit_intercept=True,
#  max_iter=1000, n_alphas=100, n_jobs=1, normalize=False, positive=False,
#  precompute='auto', random_state=None, selection='cyclic', tol=0.0001,
#  verbose=False)
# 估计器自动选择它的 lambda:
s4=lasso.alpha_
# 0.01229...

print