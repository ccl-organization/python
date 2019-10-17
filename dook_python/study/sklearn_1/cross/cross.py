# -*- coding: UTF-8 -*-
import numpy

from sklearn import svm
from sklearn import datasets
s1=numpy.arange(0,1,0.1)
s2=a=([1,2],[3,4],3,4,5,6,7,8,9)
s3=s1[:-1]

digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target
svc = svm.SVC(C=1, kernel='linear')
# svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
0.97999999999999998


import numpy as np
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)
scores = list()
for k in range(3):
     # 为了稍后的 ‘弹出’ 操作，我们使用 ‘列表’ 来复制数据
     X_train = list(X_folds)
     X_test  = X_train.pop(k)
     X_train = np.concatenate(X_train)
     y_train = list(y_folds)
     y_test  = y_train.pop(k)
     y_train = np.concatenate(y_train)
     scores.append(svc.fit(X_train, y_train).score(X_test, y_test))
print(scores)
# [0.93489148580968284, 0.95659432387312182, 0.93989983305509184]

print