# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
import math
#
# # x = np.arange(2,10)
# # y = x ** 2
# #
# # plt.plot(x,y)
# # plt.show()
#
print 0.75/math.log(800000),0.05/math.log(800000),0.1/math.log(800000),0.05/math.log(800000),0.05/math.log(800000),

# # 总阅读数
# x = np.arange(2,10)
# # y = math.log(x)*55.18
# y=math.log(np.abs(x))
# plt.plot(x,y)
# plt.show()
# #
# # x=np.arange(-5,5,0.01)
# # # y = math.log(x)*55.18
# # y=math.log(x)
# # plt.plot(x,y)
# # plt.show()
#

import matplotlib.pyplot as plt
import numpy as np

# 总阅读数
x = np.arange(2, 500)
y = np.log(np.abs(x))*55.18

x2 = np.arange(2, 100000)
y2 = np.log(np.abs(x))*3.68
y3=np.log(np.abs(x))*7.36
y4=np.log(np.abs(x))*3.68
y5=np.log(np.abs(x))*3.68
plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.plot(x, y5)
plt.show()

